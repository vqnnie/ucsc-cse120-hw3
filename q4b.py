import pyrtl

if __name__ == "__main__":
    enable = pyrtl.Input(1, "enable")
    reset = pyrtl.Input(1, "reset")
    y = pyrtl.Register(2, "y")

    # TODO: define y.next logic below using the specification in Q4.b)
    # For example: y.next <<= y ^ 1 ...

    enable_value = pyrtl.select(
        enable,
        truecase = y + 1, # enable = 1, reset = 0
        falsecase = y # enable = 0, reset = 0
    )
    reset_value = pyrtl.select(
        reset,
        truecase = 0, # reset = 1, enable = X
        falsecase = enable_value # Y or Y + 1
    )

    y.next <<= reset_value

    trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=trace)
    sim.step({"reset" : 1, "enable": 0})
    
    # TODO: write more sim.step() cases here and check if the waveform matches expected y.next value
    
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 0})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 0})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 1, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 0})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 1, "enable": 1})
    sim.step({"reset" : 0, "enable": 1})
    sim.step({"reset" : 0, "enable": 0})

    trace.render_trace()