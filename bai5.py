# Dữ liệu ban đầu
student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

# --- HÀM PHỤ TRỢ (MODULAR DESIGN) ---
def find_student(records, student_id):
    """Tìm kiếm học viên bằng ID. Chuẩn hóa ID in hoa và xóa khoảng trắng."""
    standardized_id = str(student_id).strip().upper()
    for index, student in enumerate(records):
        if student["student_id"] == standardized_id:
            return index
    return -1

# --- CÁC HÀM CHỨC NĂNG CHÍNH ---

def display_statements(records):
    """1. Hiển thị sao kê điểm số"""
    print("\n--- SAO KÊ ĐIỂM SỐ ---")
    for i, student in enumerate(records, start=1):
        points = student["current_points"]
        
        # Xác định trạng thái dựa trên điểm
        if points < 500:
            status = "Cần tích lũy thêm"
        elif 500 <= points <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"
            
        print(f"{i}. Mã: {student['student_id']} | "
              f"Tên: {student['name']} | "
              f"Hiện có: {student['current_points']} | "
              f"Đã tiêu: {student['spent_points']} | "
              f"Hoàn trả: {student['refunded_points']} | "
              f"Hệ số: x{student['multiplier']} | "
              f"Trạng thái: {status}")
    print("----------------------")

def redeem_rewards(records):
    """2. Đổi điểm lấy phần thưởng"""
    stu_id = input("Nhập mã học viên đổi quà: ")
    idx = find_student(records, stu_id)
    if idx == -1:
        print(">> Lỗi: Không tìm thấy hồ sơ học viên!")
        return

    student = records[idx]
    try:
        points_to_spend = int(input("Nhập số điểm cần tiêu: "))
        if points_to_spend <= 0:
            print(">> Lỗi: Vui lòng nhập số nguyên dương!")
            return
            
        if points_to_spend > student["current_points"]:
            print(">> Lỗi: Số dư điểm không đủ để thực hiện giao dịch!")
            return
            
        # Cập nhật dữ liệu
        student["current_points"] -= points_to_spend
        student["spent_points"] += points_to_spend
        print(f">> Giao dịch thành công! '{student['name']}' đã tiêu {points_to_spend} điểm. "
              f"Số dư còn lại: {student['current_points']} điểm.")
              
    except ValueError:
        print(">> Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

def appeal_score(records):
    """3. Phúc khảo bài thi (Hoàn điểm)"""
    stu_id = input("Nhập mã học viên cần phúc khảo: ")
    idx = find_student(records, stu_id)
    if idx == -1:
        print(">> Lỗi: Không tìm thấy hồ sơ học viên!")
        return

    student = records[idx]
    try:
        points_to_refund = int(input("Nhập số điểm hoàn lại: "))
        if points_to_refund <= 0:
            print(">> Lỗi: Vui lòng nhập số nguyên dương!")
            return
            
        if points_to_refund > student["spent_points"]:
            print(">> Lỗi: Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
            return
            
        # Cập nhật dữ liệu
        student["spent_points"] -= points_to_refund
        student["current_points"] += points_to_refund
        student["refunded_points"] += points_to_refund
        print(f">> Hoàn điểm thành công! '{student['name']}' được cộng lại {points_to_refund} điểm.")
        
    except ValueError:
        print(">> Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

def activate_multiplier(records):
    """4. Kích hoạt (Hệ số nhân điểm)"""
    stu_id = input("Nhập mã học viên nhận hệ số: ")
    idx = find_student(records, stu_id)
    if idx == -1:
        print(">> Lỗi: Không tìm thấy hồ sơ học viên!")
        return

    student = records[idx]
    try:
        new_multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))
        if new_multiplier < 1.0 or new_multiplier > 3.0:
            print(">> Lỗi: Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0!")
            return
            
        student["multiplier"] = new_multiplier
        print(f">> Đã kích hoạt hệ số x{new_multiplier} cho học viên '{student['name']}'.")
        
    except ValueError:
        print(">> Lỗi: Hệ số nhân không hợp lệ. Chỉ chấp nhận số thực từ 1.0 đến 3.0 (ví dụ: 1.5)!")

def grade_assignment(records):
    """5. Chấm bài (thêm điểm)"""
    stu_id = input("Nhập mã học viên vừa nộp bài: ")
    idx = find_student(records, stu_id)
    if idx == -1:
        print(">> Lỗi: Không tìm thấy hồ sơ học viên!")
        return

    student = records[idx]
    try:
        base_score = int(input("Nhập số điểm gốc đạt được: "))
        if base_score <= 0:
            print(">> Lỗi: Điểm gốc phải là số nguyên dương!")
            return
            
        # Tính điểm thực nhận, ép kiểu int để số điểm luôn là số nguyên
        real_score = int(base_score * student["multiplier"])
        student["current_points"] += real_score
        
        print(f">> Hệ số hiện tại của '{student['name']}' là x{student['multiplier']}. "
              f"Điểm thực nhận: {real_score}.")
        print(f">> Đã cộng {real_score} điểm vào tài khoản!")
        
    except ValueError:
        print(">> Lỗi: Vui lòng nhập số điểm gốc là một số nguyên hợp lệ!")

def main():
    """Menu điều hướng chính"""
    while True:
        print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
        print("1. Hiển thị sao kê điểm số")
        print("2. Đổi điểm lấy phần thưởng")
        print("3. Phúc khảo bài thi (Hoàn điểm)")
        print("4. Kích hoạt (Hệ số nhân điểm)")
        print("5. Chấm bài (thêm điểm)")
        print("6. Thoát chương trình")
        print("=====================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == '1':
            display_statements(student_records)
        elif choice == '2':
            redeem_rewards(student_records)
        elif choice == '3':
            appeal_score(student_records)
        elif choice == '4':
            activate_multiplier(student_records)
        elif choice == '5':
            grade_assignment(student_records)
        elif choice == '6':
            print("\nCảm ơn bạn đã sử dụng Hệ thống Ngân hàng điểm số Rikkei Academy. Tạm biệt!")
            break
        else:
            print(">> Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")

# Entry point
if __name__ == "__main__":
    main()
