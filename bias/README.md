# README

## Impersonate a Pixel 2 using a Linux laptop and a CYW920819 devboard

The attack setup assumes that the Linux laptop is able to enable diagnostic mode on the devboard,
parse diagnostic messages from the CYW920819 devboard, and run
[internalblue](https://github.com/seemoo-lab/internalblue).

To run the attacks while impersonating a Pixel 2follow those steps:

* Open `IF_PIXEL2`
    * Change the `btadd` to the Bluetooth address of the impersonated device
    * Change the `btname` to the Bluetooth name of the impersonated device
    * Change lmin and lmax to set the max and min entropy value for the
        session key ([KNOB attack](https://github.com/francozappa/knob))
* Connect the devboard to the laptop via USB
* Attach to the devboard with `btattach -B /dev/ttyUSB1 -S 115200 &`
* Enable the devboard diagnostic mode with `sudo python2 enable_diag.py`
* Start internalblue with `sudo internalblue`
* Start wireshark monitoring from internalblue
* Use `make generate` to create `bias.py`
* Use `make bias` to patch the attack device to impersonate the target
* Pair the impersonated victim (Pixel 2) and the other victim device
* Disconnect them and disable Bluetooth on the impersonated device (Pixel 2)
* Start a connection from the victim to the impersonated device (BIAS slave impersonation)
* Start a connection from the attack device to the victim (BIAS master impersonation)
* Note that during secure session establishment 
    * Mutual (secure) authentication is downgraded to unilateral (legacy) authentication
    * The attack device does not authenticate to the victim

## Other Impersonated Devices (IF.json files)

If you want to impersonate other devices you can create your own `IF.json` file
with the relevant information.

