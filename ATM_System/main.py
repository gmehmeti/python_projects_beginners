# ATM System
import atm_controller as atmCtrl


def main():
    atm = atmCtrl.ATMController(100)
    atm.run()


if __name__ == "__main__":
    main()
