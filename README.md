# GaHeal - Liquid Gallium Self-Healing PCB Trace

**Innovator:** Bhargavi Damma | Vizianagaram, Andhra Pradesh
**GitHub:** github.com/bhargavidhamma-art/GaHeal

## Problem
A micro-crack in a PCB trace causes complete device failure.
This is critical in medical devices, aerospace, defence and consumer electronics.
Current repair is slow, expensive and requires full board replacement.

## Solution
GaHeal uses Liquid Gallium, a non-toxic liquid metal with high electrical conductivity.
When applied to a cracked trace, Gallium flows into the gap and restores electrical continuity within 5 seconds, without heating or soldering.

## Validated Results

| Parameter | Cracked State | Healed State |
| :--- | :--- | :--- |
| Resistance | 1,000,000 Ohm | 1.2 Ohm |
| LED Indicator | OFF | ON |
| Buzzer Alert | ON | OFF |
| Healing Time | - | 5 Seconds |

## Validation
- Verilog HDL Simulation for crack detection logic
- Python Data Analysis for resistance vs time graph
- All source code available in this repository

## Files in this Repository
- `gaheal_test.v` - Verilog simulation for crack detection and LED/Buzzer logic
- `gaheal_graph.py` - Python script to plot resistance drop from crack to heal
- `README.md` - Project documentation

## How to Run

**Verilog:**
```bash
iverilog -o gaheal_test gaheal_test.v
vvp gaheal_test
