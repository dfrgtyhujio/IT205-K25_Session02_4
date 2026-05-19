age = int(input("Nhập tuổi bệnh nhân: "))
systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

    
if age < 75 and (90 <= systolic_bp <= 140) and blood_sugar < 150:
    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
else:
    print("TỪ CHỐI PHẪU THUẬT")
