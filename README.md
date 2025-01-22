# Self-biased-LDO

## Literature Survey

### Adaptively Biased Output Cap-Less NMOS LDO With 19 ns Settling Time:- 
No external Capacitor, fast settling NMOS LDO , adaptively biased error amplifier. This increases the loop bandwidth and slew rate of the LDO by 100% without changing no load quiscient current. Includes charge pump block in schematic. ( 180 nm )
What have they done:- Adaptive biasing of the error amplifier (EA) adjusts the bias current dynamically based on load conditions to improve bandwidth and slew rate. An NMOS-based regulation stage ensures low output impedance, faster slew rate, and improved load transient response. A cross-coupled common-gate (CG) input stage and folded-cascode (FC) output stage provide wide bandwidth and high DC gain. A fully integrated low-dropout (LDO) regulator without requiring external load capacitors.
How have they done it:- Dynamically increases the bias current of the EA during load transients.Achieved through a sensing mechanism that mirrors a portion of the load current and feeds it into the EA biasing circuit.

### High Stability Adaptive LDO using Dynamic Load Sensing for Low Power Management of Wireless Sensor Networks:- 
What have they done:- dynamic mechanism which provides low/high bias current to the error amplifier as the load current decreases/increases. 
How have they done it:- LDO adapts and transforms from a 2-stage configuration at light-loads to a 3 stage configuration at high-load conditions for a more current efficient system

### An Adaptively Biased  LDO Regulator with 11nA Quiescent Current and 50mA Available Load:- 
What have they done:- Capacitor-less LDO with series-series positive feedback for adaptive biasing. Ultra-low quiescent current (11 nA) with a load capacity of up to 50 mA.
How have they done it:- Positive feedback bias current regulation ensures proportional bias current to load current, achieving low power consumption. Stability is inherent without requiring load capacitors, as the positive feedback loop gain is kept less than one. Additional techniques, like current cancellation, startup circuitry, and high-frequency pole insertion, ensure robustness and efficient operation across varying loads.


### An ULP and Very Efficient Adaptively Biased LDO Regulator for Harvesting Application :-
What have they done:-  An LDO regulator with adaptive biasing that adjusts the quiescent current based on load current to achieve high efficiency across a wide load range (1 μA to 3 mA).
How have they done it:- FVF cells replace constant-current sources in the error amplifier, allowing the SR to improve without requiring a high fixed bias current.

### Design of an Adaptively Biased Low-Dropout Regulator With a Current Reusing Current-Mode OTA Using an Intuitive Analysis Method:-  
What have they done:- A current reusing current-mode OTA (CRCM-OTA) with high current efficiency is proposed to apply to AB-LDO.
How have they done it:- This section proposes a CRCM-OTA for AB-LDO, which is modified by CM-OTA.



# Self-Biased LDO

## Literature Survey

| **Paper Title**                                                                 | **What Have They Done**                                                                                           | **How Have They Done It**                                                                                                                                    | **Technology Node** |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| **Adaptively Biased Output Cap-Less NMOS LDO With 19 ns Settling Time**         | No external capacitor, fast settling NMOS LDO with adaptively biased error amplifier to increase loop bandwidth and slew rate by 100%.                  | Dynamically increases the bias current of the error amplifier (EA) during load transients using a sensing mechanism that mirrors a portion of the load current. | 180 nm              |
| **High Stability Adaptive LDO using Dynamic Load Sensing for Low Power Management of Wireless Sensor Networks** | Dynamic mechanism providing low/high bias current to the error amplifier as the load current decreases/increases.                                        | LDO adapts from a 2-stage configuration at light loads to a 3-stage configuration at high loads for a more current-efficient system.                          | Not Mentioned       |
| **An Adaptively Biased LDO Regulator with 11nA Quiescent Current and 50mA Available Load** | Capacitor-less LDO with series-series positive feedback for adaptive biasing. Ultra-low quiescent current (11 nA) with a load capacity of up to 50 mA.  | Positive feedback bias current regulation ensures proportional bias current to load current. Includes current cancellation, startup circuitry, and stability features. | 180 nm              |
| **An ULP and Very Efficient Adaptively Biased LDO Regulator for Harvesting Application** | LDO regulator with adaptive biasing that adjusts quiescent current based on load current for high efficiency over 1 μA to 3 mA load range.              | FVF cells replace constant-current sources in the error amplifier, improving the slew rate without requiring a high fixed bias current.                        | Not Mentioned       |
| **Design of an Adaptively Biased Low-Dropout Regulator With a Current Reusing Current-Mode OTA Using an Intuitive Analysis Method** | Proposed a current reusing current-mode OTA (CRCM-OTA) for use in adaptively biased LDOs (AB-LDOs).                                                      | Introduced a CRCM-OTA for AB-LDO, modified from the current-mode OTA (CM-OTA).                                                                               | Not Mentioned       |




