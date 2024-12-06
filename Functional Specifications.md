# Functional Specification Draft

## 1.	Background:

An enzyme-linked immunosorbent assay or ELISA is used to identify and/or quantify proteins. Given its detection abilities, it is highly useful for diagnosing various diseases from immune system disorders to infections. There are multiple different varieties of ELISAs, however one of the most commonly used is the direct sandwich ELISA. In this method the antigen of choice binds to a capture antibody. The capture antibody - antigen complex then binds to another antibody, termed the detection antibody. The detection antibody is linked to an enzyme. When a substrate is introduced, the enzyme on the detection antibody converts the substrate to a colorimetric product and the amount of signal is used to quantify the amount of antigen in the mixture. ELISA development and optimization requires researchers to perform benchtop experiments that are often cumbersome and necessitate many sequential experiments to determine the best concentrations and settings for each species. This tool allows the user to mimic the mechanisms of a direct sandwich ELISA which can aide when deciding to choose initial species concentration, temperature conditions, and which reaction variables to adjust to obtain an optimal reaction time.
 
Figure 1: The antigen binds to a capture antibody. The capture antibody - antigen complex then binds to another antibody, termed the detection antibody. The detection antibody is linked to an enzyme. When a substrate is introduced, the enzyme on the detection antibody converts the substrate to a colorimetric product and the amount of signal is used to quantify the amount of antigen in the mixture. 
Sourced from https://www.antibody-creativebiolabs.com/sandwich-elisa-with-streptavidin-biotin-detection.htm

## 2.	User profile:

There are two main user groups:
1.	Researchers with a general knowledge of sandwich ELISAs and assay development. Generally, these users are predicted to have programming experience in python.
2.	Given that the information is packaged into a user-friendly GUI the tool can also be used by users with minimal python knowledge who want to use the package to learn more about how an ELISA works. They may also not be very knowledgeable about the sandwich ELISA steps so the program provides clear documentation.

## 3.	Use cases:
1.	A researcher in a lab who does ELISA assay development wants to use this program to study how changing the concentration of capture antibody will relationally affect the final concentrations of the other species.
i.	They open their python IDE and open a new file
ii.	In their terminal they install the model_ELISA package with pip install model_ELISA
iii.	They type in “from model_ELISA import model_ELISA_gui” at the top of their code. 
iv.	Below that they type in “model_ELISA_gui.run()”
v.	They run their code
vi.	The GUI will pop up (see image below)
