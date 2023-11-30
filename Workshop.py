import os
def create_file():
    file_name = input("ป้อนชื่อไฟล์วิชาเผื่อเก็บข้อมูลคะแนน ตัวอย่าง (xxxxx.txt) : ")
    if not file_name.endswith(".txt"):
        print("""
***********************************************
******* ชื่อ-นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่ ******
***********************************************
""")
        return
    with open(file_name, "w") as file:
        print(f"ไฟล์ {file_name} ถูกสร้างขึ้นแล้ว")
        student_name = input("ป้อนชื่อ-สกุลนักเรียน : ")
        midterm_score = float(input("ป้อนคะแนนสอบกลางภาค : "))
        final_score = float(input("ป้อนคะแนนสอบปลายภาค : "))
        quiz_score = float(input("ป้อนคะแนนเก็บ : "))
        total_score = midterm_score + final_score + quiz_score
        result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"
        
        file.write(f"ชื่อ-สกุลนักเรียน : {student_name}\nคะแนนสอบกลางภาค : {midterm_score}\nคะแนนสอบปลายภาค : {final_score}\nคะแนนเก็บ : {quiz_score}\nคะแนนรวมทั้งหมด : {total_score}\nผลการเรียน : {result}\n")
        print("""
***********************************************
************* บันทึกข้อมูลเรียบร้อยแล้ว **************
***********************************************
""")
def display_files():
    files = [file for file in os.listdir() if file.endswith(".txt")]
    if not files:
        print("""
***********************************************
************** ไม่มีไฟล์ใดๆ อยู่เลย ****************
***********************************************
""")
        return
    print("ไฟล์ทั้งหมด :")
    for file in files:
        print(file)
def choose_file():
    display_files()
    file_name = input("เลือกไฟล์ : ")

    if file_name not in os.listdir():
        print("""
***********************************************
************** คุณพิมพ์ชื่อไฟล์ผิด *****************
***********************************************              
""")
        return None
    return file_name
def add_data_to_file():
    file_name = choose_file()
    if file_name:
        with open(file_name, "a") as file:
            student_name = input("ป้อนชื่อ-สกุลนักเรียน : ")
            midterm_score = float(input("ป้อนคะแนนสอบกลางภาค : "))
            final_score = float(input("ป้อนคะแนนสอบปลายภาค : "))
            quiz_score = float(input("ป้อนคะแนนเก็บ : "))

            total_score = midterm_score + final_score + quiz_score
            result = "ผ่าน" if total_score > 50 else "ไม่ผ่าน"

            file.write(f"ชื่อ-สกุลนักเรียน : {student_name}\nคะแนนสอบกลางภาค : {midterm_score}\nคะแนนสอบปลายภาค : {final_score}\nคะแนนเก็บ : {quiz_score}\nคะแนนรวมทั้งหมด : {total_score}\nผลการเรียน : {result}\n")
            print("""
***********************************************
********** เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว *********
***********************************************
""")
def read_data_from_file():
    file_name = choose_file()

    if file_name:
        with open(file_name, "r") as file:
            print(file.read())
def delete_file():
    file_name = choose_file()

    if file_name:
        os.remove(file_name)
        print("ลบไฟล์เรียบร้อยแล้ว")
def main():
    while True:
        print("""
***********************************************
****************** SCHOOL *********************
***********************************************
        [1] สร้างไฟล์วิชาใหม่เพื่อข้อมูล
        [2] เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์
        [3] เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล
        [4] เลือกวิชาและลบไฟล์
        [0] จบการทำงาน
***********************************************
""")
        choice = input("กรุณาเลือกเมนู [1] , [2] , [3] , [4] , [0] : ")
        if choice == "1":
            create_file()
        elif choice == "2":
            add_data_to_file()
        elif choice == "3":
            read_data_from_file()
        elif choice == "4":
            delete_file()
        elif choice == "0":
            print("จบการทำงานของโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
if __name__ == "__main__":
    main()

    