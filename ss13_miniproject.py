parking_lot = []
next_id = 1

while True:
    print("\n" + "="*45)
    print("QUẢN LÝ BÃI XE - SMART PARKING".center(45))
    print("="*45)
    print("1. Check-in (Đăng ký xe vào)")
    print("2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("3. Tìm kiếm xe (Theo biển số)")
    print("4. Check-out (Xử lý xe ra & Tính phí)")
    print("5. Thoát chương trình")
    print("="*45)

    choice_str = input("Nhập lựa chọn của bạn (1-5): ").strip()
    if not choice_str.isdigit():
        print("[ERR-01]: Lựa chọn không hợp lệ. Vui lòng nhập số nguyên từ 1-5!")
        continue
    
    choice = int(choice_str)

    if choice == 1:
        plate = input("Nhập biển số: ").strip()
        if not plate:
            print("[ERR-02]: Biển số không được để trống!")
            continue

        # Kiểm tra trùng biển số
        is_duplicate = False
        for car in parking_lot:
            if car['plate'] == plate:
                is_duplicate = True
                break

        if is_duplicate:
            print("[ERR-03]: Xe với biển số này đã tồn tại trong bãi!")
            continue

        # Nhập và kiểm tra loại xe
        while True:
            car_type_str = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if not car_type_str:
                print("[ERR-02]: Loại xe không được để trống!")
                continue
            if car_type_str.isdigit() and int(car_type_str) in [1, 2]:
                car_type = int(car_type_str)
                break
            print("[ERR-01]: Loại xe không hợp lệ (Vui lòng nhập 1 hoặc 2)!")

        # Nhập và kiểm tra giờ vào
        while True:
            entry_time_str = input("Nhập giờ vào (0-24): ").strip()
            if not entry_time_str:
                print("[ERR-02]: Giờ vào không được để trống!")
                continue
            if entry_time_str.isdigit():
                entry_time = int(entry_time_str)
                if 0 <= entry_time <= 24:
                    break
                else:
                    print("[ERR-01]: Giờ vào phải nằm trong khoảng từ 0 đến 24!")
                    continue
            print("[ERR-01]: Vui lòng nhập số nguyên cho giờ vào.")

        # Thêm bản ghi vào danh sách
        parking_lot.append({
            'id': next_id,
            'plate': plate,
            'type': car_type,
            'entry_time': entry_time
        })
        print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi.")
        next_id += 1

    elif choice == 2:
        if len(parking_lot) == 0:
            print("\n[Thông báo]: Bãi xe hiện đang trống!")
        else:
            print("\n{:<5} | {:<15} | {:<10} | {:<10}".format("ID", "Biển số xe", "Loại xe", "Giờ vào"))
            print("-" * 50)
            for car in parking_lot:
                type_str = "Xe máy" if car['type'] == 1 else "Ô tô"
                print("{:<5} | {:<15} | {:<10} | {:<10}".format(car['id'], car['plate'], type_str, car['entry_time']))

    elif choice == 3:
        search_plate = input("Nhập biển số xe cần tìm: ").strip()
        if not search_plate:
            print("[ERR-02]: Biển số xe tìm kiếm không được để trống!")
            continue
            
        found = False
        for car in parking_lot:
            if car['plate'] == search_plate:
                type_str = "Xe máy" if car['type'] == 1 else "Ô tô"
                print(f"\n[Tìm thấy] Thông tin chi tiết xe:")
                print(f" - ID: {car['id']}\n - Biển số: {car['plate']}\n - Loại xe: {type_str}\n - Giờ vào: {car['entry_time']}")
                found = True
                break
        if not found:
            print(f"[ERR-04]: Không tìm thấy biển số {search_plate} trong hệ thống!")

    elif choice == 4:
        checkout_plate = input("Nhập biển số xe cần ra: ").strip()
        if not checkout_plate:
            print("[ERR-02]: Biển số xe không được để trống!")
            continue
            
        car_to_checkout = None
        for car in parking_lot:
            if car['plate'] == checkout_plate:
                car_to_checkout = car
                break
                
        if car_to_checkout == None:
            print(f"[ERR-04]: Không tìm thấy biển số {checkout_plate} trong hệ thống!")
            continue
            
        # Nhập và kiểm tra giờ ra
        while True:
            exit_time_str = input("Nhập giờ ra: ").strip()
            if not exit_time_str:
                print("[ERR-02]: Giờ ra không được để trống!")
                continue
            if exit_time_str.isdigit():
                exit_time = int(exit_time_str)
                if exit_time < car_to_checkout['entry_time']:
                    print("[ERR-05]: Giờ ra phải sau hoặc bằng giờ vào!")
                    continue
                break
            print("[ERR-01]: Vui lòng nhập số nguyên cho giờ ra.")
                
        # Tính phí
        rate = 5000 if car_to_checkout['type'] == 1 else 10000
        fee = (exit_time - car_to_checkout['entry_time']) * rate
        
        print(f"\nTổng phí phải trả: {fee} VNĐ")
        
        # Xóa xe khỏi bãi
        parking_lot.remove(car_to_checkout)
        print(f"[Thành công]: Đã xử lý check-out và xóa xe ID {car_to_checkout['id']} khỏi hệ thống!")

    elif choice == 5:
        print("Đã thoát chương trình. Tạm biệt!")
        break

    else:
        print("[ERR-01]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")