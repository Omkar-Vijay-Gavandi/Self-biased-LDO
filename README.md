# Self-biased-LDO

## Literature Survey



| **Paper Title**                                                                 | **What Have They Done**                                                                                           | **How Have They Done It**                                                                                                                                    | **Technology Node** |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| **Adaptively Biased Output Cap-Less NMOS LDO With 19 ns Settling Time**         | No external capacitor, fast settling NMOS LDO with adaptively biased error amplifier to increase loop bandwidth and slew rate by 100%.                  | Dynamically increases the bias current of the error amplifier (EA) during load transients using a sensing mechanism that mirrors a portion of the load current. | 180 nm              |
| **High Stability Adaptive LDO using Dynamic Load Sensing for Low Power Management of Wireless Sensor Networks** | Dynamic mechanism providing low/high bias current to the error amplifier as the load current decreases/increases.                                        | LDO adapts from a 2-stage configuration at light loads to a 3-stage configuration at high loads for a more current-efficient system.                          | 65nm       |
| **An Adaptively Biased LDO Regulator with 11nA Quiescent Current and 50mA Available Load** | Capacitor-less LDO with series-series positive feedback for adaptive biasing. Ultra-low quiescent current (11 nA) with a load capacity of up to 50 mA.  | Positive feedback bias current regulation ensures proportional bias current to load current. Includes current cancellation, startup circuitry, and stability features. | 180 nm              |
| **An ULP and Very Efficient Adaptively Biased LDO Regulator for Harvesting Application** | LDO regulator with adaptive biasing that adjusts quiescent current based on load current for high efficiency over 1 μA to 3 mA load range.              | FVF cells replace constant-current sources in the error amplifier, improving the slew rate without requiring a high fixed bias current.                        | 130nm      |
| **Design of an Adaptively Biased Low-Dropout Regulator With a Current Reusing Current-Mode OTA Using an Intuitive Analysis Method** | Proposed a current reusing current-mode OTA (CRCM-OTA) for use in adaptively biased LDOs (AB-LDOs).                                                      | Introduced a CRCM-OTA for AB-LDO, modified from the current-mode OTA (CM-OTA).                                                                               | 180nm      |


Week 1 updates:-

## Week 2 Updates

### Overview
This week, I focused on understanding the functionality of the Operational Transconductance Amplifier (OTA) implemented using a folded cascode configuration. The circuit employs adaptive biasing, where transistors Md1-Md7 adjust the bias based on the load current. Currently, I am working on a two-stage configuration that remains active when the load current is below a threshold of 919µA.

### OTA Operation

![image](https://github.com/user-attachments/assets/cb5ff7d5-f588-4cb4-bd76-799e2fceaa0a)


- The PMOS transistor Md1 mirrors the current flowing in the pass transistor and dynamically adjusts the OTA’s bias as the load current varies.
- This mirrored current is then passed through a current mirror circuit, which sets the bias for the folded cascode stage.
- The circuit operates with a reference voltage of 0.6V and a supply voltage of 0.8V. Given the low supply voltage and the need for a good Power Supply Rejection Ratio (PSRR), a folded cascode configuration is used to optimize headroom.
- As the load current changes, Md1 generates a scaled version of the current to bias the OTA transistors accordingly. This ensures that all transistors remain in saturation while minimizing power consumption when no significant load is connected.

This implementation enhances power efficiency and ensures stable operation across varying load conditions.




