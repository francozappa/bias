# README

Repository about [Bluetooth Impersonation AttackS (BIAS)](https://francozappa.github.io/about-bias/).

* [Instruction to perform the BIAS attacks](https://github.com/francozappa/bias/tree/master/bias)
* [Code to patch linux-4.14.111 to enable H4 parsing](https://github.com/francozappa/bias/tree/master/linux-4.14.111)
    * Make sure to install the relevant kernel modules to interface with the
        devboard. For example, USB serial drivers and device drivers for the
        Bluetooth subsystem.
* [Code to validate the legacy authentication procedure](https://github.com/francozappa/bias/tree/master/la)
* [Code to validate the secure authentication procedure](https://github.com/francozappa/bias/tree/master/sa)

Related work:

* [BIAS: Bluetooth Impersonatoin AttackS](https://francozappa.github.io/publication/bias/) [S&P20]
* [The KNOB is Broken: Exploiting Low Entropy in the Encryption Key Negotiation of Bluetooth BR/EDR](https://francozappa.github.io/publication/knob/) [SEC19]


I'd like to thank Nils Glörfeld for his contributions to reverse-engineer
and patch the CYW920819 development board's firmware, and to patch the Linux kernel.
