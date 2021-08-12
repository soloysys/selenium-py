#coding=utf-8
Feature: Register User
    As a developer
    This is my first bdd project
    Scenario: open register website
        When I open the login website'https://xunkao.dev.pkpm.cn:9033/#/indexchild'
        Then I expect the title is "海南省"

    Scenario: input username
        When I set the useremail as "111"
        #And I set the password as "111"
        #And I set the QRcode as "test"
        #Then I expect that element contains text "验证码错误"