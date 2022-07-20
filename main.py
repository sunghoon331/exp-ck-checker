import time
import web_checker

if __name__ == '__main__':
    print("exp ck checker")

    file = open("info.txt", "r", encoding='utf8')
    strings = file.readlines()
    file.close()

    url = strings[0]
    driver = web_checker.getDriver(url)

    web_checker.login(driver, strings[1].strip(), strings[2].strip())
    time.sleep(2)
    web_checker.setUrl(driver, "https://exp.ck.ac.kr/assign/requestEmpStudentList.do")
    web_checker.close(driver)



