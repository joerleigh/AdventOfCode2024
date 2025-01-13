import re


class BunchOfGates:
    bitmask16 = (1 << 16) - 1

    def __init__(self, lines):
        self.wires = {}
        self.gates = {}
        self.parse_input(lines)

    def parse_input(self, lines):
        self.wires = {}
        self.gates = {}
        and_re = re.compile(r'^([a-z0-9]+) AND ([a-z0-9]+) -> ([a-z0-9]+)')
        or_re = re.compile(r'^([a-z0-9]+) OR ([a-z0-9]+) -> ([a-z0-9]+)')
        xor_re = re.compile(r'^([a-z0-9]+) XOR ([a-z0-9]+) -> ([a-z0-9]+)')
        lshift_re = re.compile(r'^([a-z0-9]+) LSHIFT ([a-z0-9]+) -> ([a-z0-9]+)')
        rshift_re = re.compile(r'^([a-z0-9]+) RSHIFT ([a-z0-9]+) -> ([a-z0-9]+)')
        not_re = re.compile(r'^NOT ([a-z0-9]+) -> ([a-z0-9]+)')
        eq_re = re.compile(r'^([a-z0-9]+) -> ([a-z0-9]+)')
        for line in lines:
            gate, a, b, c = None, None, None, None
            if andMatch := and_re.match(line):
                gate, a, b, c = self.and_gate, andMatch[1], andMatch[2], andMatch[3]
            elif orMatch := or_re.match(line):
                gate, a, b, c = self.or_gate, orMatch[1], orMatch[2], orMatch[3]
            elif xorMatch := xor_re.match(line):
                gate, a, b, c = self.xor_gate, xorMatch[1], xorMatch[2], xorMatch[3]
            elif lshiftMatch := lshift_re.match(line):
                gate, a, b, c = self.lshift_gate, lshiftMatch[1], int(lshiftMatch[2]), lshiftMatch[3]
            elif rshiftMatch := rshift_re.match(line):
                gate, a, b, c = self.rshift_gate, rshiftMatch[1], int(rshiftMatch[2]), rshiftMatch[3]
            elif notMatch := not_re.match(line):
                gate, a, c = self.not_gate, notMatch[1], notMatch[2]
            elif eqMatch := eq_re.match(line):
                gate, a, c = self.eq_gate, eqMatch[1], eqMatch[2]

            if gate is not None:
                self.wires[c] = None
                self.gates[c] = (gate, a, b)

    def solve(self):
        while not self.is_solved():
            self.tick()

    def tick(self):
        for output in self.gates.keys():
            gate, a, b = self.gates[output]
            self.wires[output] = gate(a, b)

    def is_solved(self):
        for wire in self.wires.keys():
            if self.wires[wire] is None:
                return False
        return True

    def and_gate(self, a, b):
        a = self.wire_value(a)
        b = self.wire_value(b)
        if a is not None and b is not None:
            return a & b & self.bitmask16

    def or_gate(self, a, b):
        a = self.wire_value(a)
        b = self.wire_value(b)
        if a is not None and b is not None:
            return a | b & self.bitmask16

    def xor_gate(self, a, b):
        a = self.wire_value(a)
        b = self.wire_value(b)
        if a is not None and b is not None:
            return a ^ b & self.bitmask16

    def lshift_gate(self, a, b):
        a = self.wire_value(a)
        b = self.wire_value(b)
        if a is not None and b is not None:
            return a << b & self.bitmask16

    def rshift_gate(self, a, b):
        a = self.wire_value(a)
        b = self.wire_value(b)
        if a is not None and b is not None:
            return a >> b & self.bitmask16

    def not_gate(self, a, b):
        a = self.wire_value(a)
        if a is not None:
            return ~ a & self.bitmask16

    def eq_gate(self, a, b):
        a = self.wire_value(a)
        if a is not None:
            return a & self.bitmask16

    def wire_value(self, a):
        if a in self.wires:
            return self.wires[a]
        if self.is_int(a):
            return int(a)
        return None

    @staticmethod
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
