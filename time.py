import sys
import os
import time

# هذا هو IDك فقط
ALLOWED_IDS = [6969145414,5972284055,6768751513,1075099303,5645022700,5415484857,7272808519,5088403034,6145336551,5877403580,6351517719]

def main():
    try:
        user_id = int(input("\x1b[1;32mENTR ID-»  \033[1;31m"))
    except ValueError:
        print("انت غير مشترك في الأداة")  # إدخال غير صالح
        sys.exit()

    if user_id in ALLOWED_IDS:
        print("\n✅ تم التحقق بنجاح، يمكنك استخدام الأداة الآن.\n");time.sleep(2)
        # ضع هنا كود أداتك الحقيقي
    else:
        print("\n❌ انت غير مشترك في الأداة.")
        sys.exit();print('\n\n[Program finished]');time.sleep(1000000000)

if __name__ == "__main__":
    main()
