Nameyou = input("Enter your name : ")
Temp = float(input("Enter your head's temp : "))

if Temp <= 25:
    status = "อากาศกำลังดีคับยัยตัวแสบ"
    action = "กล่องบุหรี่ลอยขึ้นมา"
elif Temp <= 30:
    status = "อากาศเริ่มได้เสียต้องมีพัดลมหน่อยๆ"
    action = "พัดลมเปิด!!!"
elif Temp <= 40:
    status = "เปิดแอร์ดิรอพ่อมึงมากดเปิดให้เหรอไอ้เวร"
    action = "แอร์เปิด"
else:
    status = "จองวัดได้เลยคับ"
    action = "ทักข้อความไปหาคนในครอบครัวว่าลาโลกแล้ว"

print(f"\nสวัสดีครับคุณ {Nameyou} \nอุณหภูมิของคุณ : {Temp} \n สถานะของคุณ : {status}")
print(f"คำสั่งระบบ : {action}")
