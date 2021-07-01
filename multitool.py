import nidmm
import matplotlib.pyplot as plt
import numpy as np
with nidmm.Session("Dev1") as session:
    session.configure_multi_point(trigger_count=1, sample_count=100, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=0.5)
    Volts = session.read_multi_point(array_size=100)
    Volts = list(Volts)
    print("Measurement: " + str(Volts))

    time = np.linspace(0, 100, 100)
    plt.figure(dpi=150)
    plt.plot(time, Volts, color='m', linewidth=2)
    plt.xlabel('Time', fontsize=15)
    plt.ylabel('Volts', fontsize=15)
    plt.grid()
    plt.show()

    session.abort
