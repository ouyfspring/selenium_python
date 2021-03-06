#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/23 16:53
# software: PyCharm



from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.Login_Case('test_loginsSuccess'))
    suite.addTest(credit_case.Credit_Case('test_CreditSuccess'))
    suite.addTest(card_stage_case.Card_Case('test_CardSuccess'))
    suite.addTest(company_examine_case.Company_Examine('test_ExamineSuccess'))
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineFirstSuccess'))
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineSecondSuccess'))
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineThirdSuccess'))
    return suite
