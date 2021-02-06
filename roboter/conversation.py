from roboter import robot


# Medicalconsultationの関数をそれぞれ呼び出す
def talk_about_medicalconsultation(reasons):
    medical_robot = robot.MedicalRobot()
    medical_robot.questions()
    medical_robot.write_csv(reasons)