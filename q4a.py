import pyrtl

def datapath(zero, lt, opcode):
    # TODO: implement logic to assign branch below using the specification in Q4.a)
    # For example: branch = zero & lt ~opcode
    op_l = opcode[1]; # left bit
    op_r = opcode[0]; # right bit

    branch = (
        (~op_l & ~op_r & lt) | # 00: blt
        (~op_l & op_r & ~lt) | # 01: bge, ~blt
        (op_l & ~op_r & zero) | # 10: beq
        (op_l & op_r & ~zero) # 11: bne, ~beq
    )
    return branch

if __name__ == "__main__":
    zero = pyrtl.Input(1, "zero")
    lt = pyrtl.Input(1, "lt")
    opcode = pyrtl.Input(2, "opcode")

    branch_out = datapath(zero, lt, opcode)

    branch = pyrtl.Output(1, "branch")
    branch <<= branch_out

    sim = pyrtl.Simulation()

    # Example test case below, this should PASS
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")
    
    # TODO: write test cases here

    # blt condition not met
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 0b00})
        assert sim.inspect("branch") == 0
        print("blt condition not met: PASS")
    except:
        print("blt condition not met: FAIL")

    # blt condition met
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0b00})
        assert sim.inspect("branch") == 1
        print("blt condition met: PASS")
    except:
        print("blt condition met: FAIL")

    # bge condition not met
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0b01})
        assert sim.inspect("branch") == 0
        print("bge condition not met: PASS")
    except:
        print("bge condition not met: FAIL")

    # bge condition met
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 0b01})
        assert sim.inspect("branch") == 1
        print("bge condition met: PASS")
    except:
        print("bge condition met: FAIL")

    # beq condition not met
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 0b10})
        assert sim.inspect("branch") == 0
        print("beq condition not met: PASS")
    except:
        print("beq condition not met: FAIL")

    # beq condition met
    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 0b10})
        assert sim.inspect("branch") == 1
        print("beq condition met: PASS")
    except:
        print("beq condition met: FAIL")

    # bne condition not met
    try:
        sim.step({"zero" : 1, "lt" : 0, "opcode": 0b11})
        assert sim.inspect("branch") == 0
        print("bne condition not met: PASS")
    except:
        print("bne condition not met: FAIL")

    # bne condition met
    try:
        sim.step({"zero" : 0, "lt" : 0, "opcode": 0b11})
        assert sim.inspect("branch") == 1
        print("bne condition met: PASS")
    except:
        print("bne condition met: FAIL")