from modules.system_mac import get_system_mac

def show_mac_address_interfaces_system():
    result = get_system_mac()
    print('-'*50)
    print(f"{'Interface':15} {'Mac Address':20}")  # اصلاح f-string و مرتب‌سازی
    print('-'*50)
    for iface, mac in result.items():
        print(f'{iface:19} {mac}')
    input('\nPress ENTER...')

def main():
    while True:  # حلقه اصلی برنامه
        print("\n" + "="*50)
        print("                  MacTool v0.1")
        print("="*50)
        print("1.Show MacAddress Interfaces System")
        print("2.Exit")
        print("="*50)
        
        choice = input('Choice: ').strip()
        
        if choice == '1':
            show_mac_address_interfaces_system()
        elif choice == '2':
            print("Goodbye!")
            break  # خروج از حلقه (برنامه بسته میشه)
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()