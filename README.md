This archive contains simple implementation of bitcoin address generator using Python 3.8 built-in modules, without any external library.

## Description
- `elliptic_curve.py` is implementation of the elliptic curve arithmetic
- `address_conversions.py` and `type_encodings.py` contain functions related to encodings and different forms of bitcoin addresses
- `main.py` contains definition of bitcoin curve (secp256k1) and `main()` function with step by step keys generation

## Requirements
- Python 3.8 (not tested on other versions)
## Usage
To download the repository, enter:
```
git clone https://github.com/kamsec/simple-btc-address.git
```
- Using it with command:
    ```
    python main.py
    ```
    will generate and print pair of private and public bitcoin keys using python built-in `secrets` module as a source of randomness.
    Example output:
    ```
    --------------PRIVATE KEY--------------
    Private key (int): 44717509747896394309047538484946587312654961699468994500260335569418079671640
    Private key (hex): 62DD36AE00D30B4EE5E3FCA10D244FBCBECB5286B70838A6517E77926E2F9558
    Private key (base64): Yt02rgDTC07l4/yhDSRPvL7LUoa3CDimUX53km4vlVg=
    Private key (WIF): 5JZpw3hLxVHZK4kwx3JVNSHSZmPitg2qEQFXvT7f6ZXfnRkCZAS
    Private key (WIF compressed): KzXtZYu55ur5cjayXwACDcbZqcwHu5H5t9d9UvGP9YaNBDcLtHfs
    --------------PUBLIC KEY--------------
    Public point: (39166939953508316691732955170591039199802573725376267304908758959869881762527, 72628808298061672905141035051583648853453376440284148500560293012640722841450)
    Public key (uncompressed): 045697B3D1CAA4F5016464FBEAFDC8E06928B7939EC82150FCDC5B0ADE02C442DFA09272E0900BC99820C700ABF50AD75EC1918CECF775A50E7E239AF72C3BEF6A
    Bitcoin address (uncompressed): 1L342bogCq8jMBoSz5YybQVMU1zkxMCSzS
    Public key (compressed): 025697B3D1CAA4F5016464FBEAFDC8E06928B7939EC82150FCDC5B0ADE02C442DF
    Bitcoin address (compressed): 1E3nfYzJowcauARhctkjLYSyxnavdarDGk
    ---------------------------------------
    ```

- If you have truly random integer from the correct range, the easy way of using it with this program to create keys is described in `main()` function in `main.py`. Check out the code!
