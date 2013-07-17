from skills.models import Tree
from vacancies.models import User_skills, Vacancy_skills
from django.contrib.auth.models import User


class Match():

    def matchSkills(self, vacancy, amount=100):

        skilledUsers = {}
        skillSet = {}

        for skill in [x.id for x in Vacancy_skills.objects.filter(vacancy_id = vacancy)]:
            childSkillSet = [skill]
            while True:
                childSkillSetNew = []
                for childSkill in childSkillSet:
                    children = Tree.objects.get(parent=childSkill)
                    for child in children:
                        skillSet[skill]['skills'][child.id]=child.strength
                        childSkillSetNew.append(child.id)
                if not len(childSkillSetNew):
                    break
                childSkillSet = childSkillSetNew

        for user in [ x.id for x in User.objects.all()]:
            finalSkillCount = 0.
            
            for requiredSkill in skillSet.keys():
                skillCount = 1.
                for childSkill in requiredSkill['skills'].keys():
                    if childSkill in [x.id for x in User_skills.objects.get(user_id = user)]:
                        skillCount = skillCount + 0.01*skillCount*requiredSkill['skills'][childSkill]
                finalSkillCount = finalSkillCount + skillCount/requiredSkill['skills']['count']
            if len(skilledUsers) < amount:
                skilledUsers[user] = finalSkillCount
            elif skilledUsers.values().sort()[-amount] < finalSkillCount:
                skilledUsers[user] = finalSkillCount
            if 2*amount < len(skilledUsers):
                for tmpUser in skilledUsers:
                    if skilledUsers[tmpUser] < skilledUsers.values().sort()[-amount]:
                        del skilledUsers[tmpUser]
        for tmpUser in skilledUsers:
            if skilledUsers[tmpUser] < skilledUsers.values().sort()[-amount]:
                del skilledUsers[tmpUser]
        return skilledUsers




"""
 SkillSet = {
    'python' : { 'skills' : { django : 5, } 'count':12 }, 
 }


"""
