"""Translate pre-filled WhatsApp texts on /th/ pages. Run after build_th.py."""
import sys, glob, re, urllib.parse
ASK = "รบกวนแจ้งเงื่อนไข เอกสารที่ต้องใช้ และค่าบริการก่อนครับ"
M = {
 "Hello Kevin, I would like to ask about a medical stay or medical extension in Thailand. I understand you are not taking new processing requests at the moment, and I would first like to know the conditions and documents involved.":
   "สวัสดีครับ Kevin ขอสอบถามเรื่องการพำนักหรือขยายระยะเวลาเพื่อรักษาพยาบาลในไทย ทราบว่าขณะนี้งดรับงานใหม่ชั่วคราว อยากทราบเงื่อนไขและเอกสารที่เกี่ยวข้องก่อนครับ",
 "Hello Kevin, I would like to ask about the Destination Thailand Visa (DTV). Please first explain the conditions, the documents required and the steps involved.":
   "สวัสดีครับ Kevin ขอสอบถามเรื่องวีซ่า DTV (Destination Thailand Visa) รบกวนแจ้งเงื่อนไข เอกสารที่ต้องใช้ และขั้นตอนก่อนครับ",
 "Hello Kevin, I would like to ask about the Thailand 90-day report (TM47). Please first explain the conditions, the documents required and how it is filed.":
   "สวัสดีครับ Kevin ขอสอบถามเรื่องรายงานตัว 90 วัน (ตม.47) รบกวนแจ้งเงื่อนไข เอกสารที่ต้องใช้ และวิธียื่นก่อนครับ",
 "Hello Kevin, I would like to ask about your Thailand visa services. Please first explain the eligibility, the documents required and your service fee.":
   "สวัสดีครับ Kevin ขอสอบถามเรื่องบริการวีซ่าไทย " + ASK,
 "Hello Kevin, I would like to ask about: Bangkok airport send-off service. Airport: , date: , number of travellers: .":
   "สวัสดีครับ Kevin ขอสอบถามเรื่อง: บริการส่งที่สนามบินกรุงเทพฯ สนามบิน: , วันที่: , จำนวนผู้เดินทาง: ",
}
SVC = {"Airport services":"บริการสนามบิน","Business visa":"วีซ่าธุรกิจ","Elite visa (Thailand Privilege)":"วีซ่าอีลิท (Thailand Privilege)",
       "Extensions":"ต่ออายุวีซ่า","Retirement visa":"วีซ่าเกษียณ","Student visa":"วีซ่านักเรียน","Work visa / temporary work visa":"วีซ่าทำงาน / วีซ่าทำงานชั่วคราว"}
for k,v in SVC.items():
    M["Hello Kevin, I would like to ask about: %s. Please first explain the eligibility, the documents required and your service fee." % k] = "สวัสดีครับ Kevin ขอสอบถามเรื่อง: %s %s" % (v, ASK)
left = 0
for f in glob.glob(sys.argv[1] + '/th/*.html'):
    s = open(f, encoding='utf-8').read()
    def rep(m):
        global left
        t = urllib.parse.unquote(m.group(1))
        if t not in M: left += 1; return m.group(0)
        return 'wa.me/66987390634?text=' + urllib.parse.quote(M[t])
    s = re.sub(r'wa\.me/66987390634\?text=([^"&]*)', rep, s)
    open(f, 'w', encoding='utf-8').write(s)
print('untranslated WhatsApp texts left:', left)
