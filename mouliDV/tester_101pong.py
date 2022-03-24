#!/bin/python3

from pickle import TRUE
from pydoc import describe
import subprocess
import sys
import os
from moulitek.moulitek import *

argv = sys.argv
# executable_name = "101pong-right-answer"
executable_name = "101pong"

if not os.path.exists(executable_name) :
    exit()

trace = {
#help test
"help" : [False, ""],
#rigor test
"1a": [False, ""],
"1b": [False, ""],
"1c": [False, ""],
"1d": [False, ""],
"1e": [False, ""],
"1f": [False, ""],
"1g": [False, ""],
"1h": [False, ""],
"1i": [False, ""],
"1j": [False, ""],
#vector test
"2a": [False, ""],
"2b": [False, ""],
"2c": [False, ""],
"2d": [False, ""],
"2e": [False, ""],
#trigonométrie test
"3a": [False, ""],
"3b": [False, ""],
"3c": [False, ""],
"3d": [False, ""],
"3e": [False, ""],
#mathematical_rigor
"4a": [False, ""],
"4b": [False, ""],
"4c": [False, ""],
"4d": [False, ""],
"4e": [False, ""],
}

if not os.path.exists("temp/") :
    os.mkdir("temp")

def rigor_binar_test(tested_value, name_id, result, reason, sequence, test_name):
    global trace
    if result == tested_value:
        trace[name_id][0] = True
        sequence.set_status(test_name, passed=True)
    else :
        trace[name_id][1] = reason

def result_test(tested_value, name_id, result, sequence, test_name):
    global trace
    user_answer = open("temp/tested_prog_output", "r")
    user_answer = user_answer.read()
    user_answer = "".join(user_answer.split(")")[:-1])
    user_answer = user_answer + ")"

    right_answer = open("mouliDV/right_answer/" + name_id, "r")
    right_answer = right_answer.read()
    right_answer = "".join(right_answer.split(")")[:-1])
    right_answer = right_answer + ")"

    if result != tested_value:
        trace[name_id][1] = "wrong return value : got " + (str)(result) + " expected : " + (str)(tested_value)
        sequence.set_status(test_name, passed=False, reason=RETVALUE, expected=(str)(tested_value), got=(str)(result))
        return
    if right_answer != user_answer:
        trace[name_id][1] = "wrong result or disposition"
        sequence.set_status(test_name, passed=False, reason=BADOUTPUT, expected=right_answer, got=user_answer)
        return
    if result == tested_value and right_answer == user_answer:
        trace[name_id][0] = True
        sequence.set_status(test_name, passed=True)

def result_test_colision(tested_value, name_id, result, sequence, test_name):
    global trace
    user_answer = open("temp/tested_prog_output", "r")
    user_answer = user_answer.read()

    right_answer = open("mouliDV/right_answer/" + name_id, "r")
    right_answer = right_answer.read()

    if result != tested_value:
        trace[name_id][1] = "wrong return value : got " + (str)(result) + " expected : " + (str)(tested_value)
        sequence.set_status(test_name, passed=False, reason=RETVALUE, expected=(str)(tested_value), got=(str)(result))
        return
    if not "The incidence angle is:" in user_answer:
        sequence.set_status(test_name, passed=False, reason=BADOUTPUT, expected=right_answer, got=user_answer)
        trace[name_id][1] = "wrong syntaxe"
        return
    if result == tested_value and right_answer == user_answer:
        trace[name_id][0] = True
        sequence.set_status(test_name, passed=True)

def result_tricky_test(tested_value, name_id, result, sequence, test_name):
    global trace
    user_answer = open("temp/tested_prog_output", "r")
    user_answer = user_answer.read()

    right_answer = open("mouliDV/right_answer/" + name_id, "r")
    right_answer = right_answer.read()

    if result != tested_value:
        trace[name_id][1] = "wrong return value : got " + (str)(result) + " expected : " + (str)(tested_value)
        sequence.set_status(test_name, passed=False, reason=RETVALUE, expected=(str)(tested_value), got=(str)(result))
        return
    if right_answer != user_answer:
        trace[name_id][0] = True
        sequence.set_status(test_name, passed=False, reason=RETVALUE, expected=right_answer, got=user_answer)
        return
    if result == tested_value and right_answer == user_answer:
        trace[name_id][0] = True
        sequence.set_status(test_name, passed=True)

def test_help():
    help_categorie = Category("0-Help", "check the good shape of the usage")
    help_sequence = help_categorie.add_sequence("Usage", "check the good shape of the -h")
    help_sequence.add_test("usage 1", "check the good shape of the -h")
    os.system("./" + executable_name + " -h" + " > temp/tested_prog_output")
    temp_answer = open("temp/tested_prog_output", "r")
    temp_answer = temp_answer.read()
    temp_answer = "".join(temp_answer.split(")")[:-1])
    temp_answer =temp_answer + ")"

    right_answer = open("mouliDV/right_answer/help", "r")
    right_answer = right_answer.read()
    right_answer = "".join(right_answer.split(")")[:-1])
    right_answer = right_answer + ")"
    if temp_answer == right_answer :
        trace["help"][0] = True
        help_sequence.set_status("usage 1", passed=True)
    if temp_answer != right_answer :
        help_sequence.set_status("usage 1", passed=False, reason=BADOUTPUT, expected="OK", got="KO")

def rigor():
    rigor_category = Category("1-rigor", "check the rigor of how you write your results")

    #no argument
    test_name = "no argument"
    description = "test your programme without argument"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name, shell=True)
    rigor_binar_test(84, "1a", result, "wrong return value when no argument", rigor_sequence, test_name)

    #not enough arguments
    test_name = "not enought arguments"
    description = "test your programme without enought argument"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 15 8", shell=True)
    rigor_binar_test(84, "1b", result, "wrong return value when not enought argument", rigor_sequence, test_name)

    #to many argument
    test_name = "to many arguments"
    description = "test your programme with to many arguments"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 15 8 5 8 45 78 34 0", shell=True)
    rigor_binar_test(84, "1c", result, "wrong return value when to many argument", rigor_sequence, test_name)

    #incorrect argument
    test_name = "incorrect argument"
    description = "test your programme with incorrects arguments"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 15 8 5 8 salut 78 34", shell=True)
    rigor_binar_test(84, "1d", result, "wrong return value when incorect argument", rigor_sequence, test_name)

    #negative time shift
    test_name = "negative time shift"
    description = "test your programme with a negative time shift"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 1 2 3 4 5 6 -4", shell=True)
    rigor_binar_test(84, "1e", result, "wrong return value when negative value for the time shift", rigor_sequence, test_name)

    #float time shift
    test_name = "float time shift"
    description = "test your programme with a float for the time shift"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 1 2 3 4 5 6 4.2", shell=True)
    rigor_binar_test(84, "1f", result, "wrong return value when float value for the time shift", rigor_sequence, test_name)

    #output rigour 1
    test_name = "output rigour 1"
    description = "test how you write your result"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 1 1 1 1 1 1 1" + " > temp/tested_prog_output", shell=True)
    result_test(84, "1g", result, rigor_sequence, test_name)

    #output rigour 2
    test_name = "output rigour 2"
    description = "test how you write your result"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 1 1 1 3 3 3 5" + " > temp/tested_prog_output", shell=True)
    result_test(0, "1h", result, rigor_sequence, test_name)

    #output rigour 3
    test_name = "output rigour 3"
    description = "test how you write your result"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 3 3 3 1 1 1 1" + " > temp/tested_prog_output", shell=True)
    result_test(0, "1i", result, rigor_sequence, test_name)

    #output rigour 4
    test_name = "output rigour 4"
    description = "test how you write your result"
    rigor_sequence = rigor_category.add_sequence(test_name, description)
    rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 9186 1368 2539 7757 8063 4392 69" + " > temp/tested_prog_output", shell=True)
    result_test(0, "1j", result, rigor_sequence, test_name)

def vector():
    vector_category = Category("2-vector", "check if your answers are right")

    #vector coordinates 1
    test_name = "vector coordinates 1"
    description = "check if your answer is good with integers numbers has argument"
    vector_sequence = vector_category.add_sequence(test_name, description)
    vector_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 0 0 0 10 10 10 2" + " > temp/tested_prog_output", shell=True)
    result_test(0, "2a", result, vector_sequence, test_name)

    #vector coordinates 2
    test_name = "vector coordinates 2"
    description = "check if your answer is good with integers numbers has argument"
    vector_sequence = vector_category.add_sequence(test_name, description)
    vector_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 28 55 70 32 19 95 7" + " > temp/tested_prog_output", shell=True)
    result_test(0, "2b", result, vector_sequence, test_name)

    #vector coordinates 3
    test_name = "vector coordinates 3"
    description = "check if your answer is good with integers numbers has argument"
    vector_sequence = vector_category.add_sequence(test_name, description)
    vector_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 0 600 194 979 84 537 86" + " > temp/tested_prog_output", shell=True)
    result_test(0, "2c", result, vector_sequence, test_name)

    #vector coordinates floats 1
    test_name = "vector coordinates float 1"
    description = "check if your answer is good with float numbers has argument"
    vector_sequence = vector_category.add_sequence(test_name, description)
    vector_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 12.5 74.6 13 59.3 42.6 44.1 7" + " > temp/tested_prog_output", shell=True)
    result_test(0, "2d", result, vector_sequence, test_name)

    #vector coordinates floats 1
    test_name = "vector coordinates float 2"
    description = "check if your answer is good with float numbers has argument"
    vector_sequence = vector_category.add_sequence(test_name, description)
    vector_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 5220.196 3128.846 1841.693 2520.51 6973.101 3496.550 817" + " > temp/tested_prog_output", shell=True)
    result_test(0, "2e", result, vector_sequence, test_name)

def trigonometrie():
    trigonometrie_category = Category("3-trigonometrie", "check if your incidences angles are right")

    #incident angle float 1
    test_name = "incident angle float 1"
    description = "check if your incidences angles is right"
    trigonometrie_sequence = trigonometrie_category.add_sequence(test_name, description)
    trigonometrie_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 3 3 3 1 1 1 2" + " > temp/tested_prog_output", shell=True)
    result_test_colision(0, "3a", result, trigonometrie_sequence, test_name)

    #incident angle float 2
    test_name = "incident angle float 2"
    description = "check if your incidences angles is right"
    trigonometrie_sequence = trigonometrie_category.add_sequence(test_name, description)
    trigonometrie_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 4 4 5 4 6 4 2" + " > temp/tested_prog_output", shell=True)
    result_test_colision(0, "3b", result, trigonometrie_sequence, test_name)

    # #incident angle 1
    # test_name = "incident angle 1"
    # description = "check if your incidences angles is right"
    # trigonometrie_sequence = trigonometrie_category.add_sequence(test_name, description)
    # trigonometrie_sequence.add_test(test_name, description)
    # result = subprocess.call("./" + executable_name + " 4 4 5 4 6 4 2" + " > temp/tested_prog_output", shell=True)
    # result_test_colision(0, "3c", result, trigonometrie_sequence, test_name)

def mathematical_rigor():
    mathematical_rigor_categorie = Category("4-mathematical rigor", "check somme tricky values")

    # #speed vector with z = 0
    # test_name = "speed vector with z = 0"
    # description = "check the vector when z = 0"
    # mathematical_rigor_sequence = mathematical_rigor_categorie.add_sequence(test_name, description)
    # mathematical_rigor_sequence.add_test(test_name, description)
    # result = subprocess.call("./" + executable_name + " 4 4 5 4 6 4 2" + " > temp/tested_prog_output", shell=True)
    # result_tricky_test(0, "4a", result, mathematical_rigor_sequence, test_name)

    #speed vector with z = 0
    test_name = "0 degree angle"
    description = "check the result when the incidence angle is 0"
    mathematical_rigor_sequence = mathematical_rigor_categorie.add_sequence(test_name, description)
    mathematical_rigor_sequence.add_test(test_name, description)
    result = subprocess.call("./" + executable_name + " 1 1 1 1 2 1 2" + " > temp/tested_prog_output", shell=True)
    result_tricky_test(0, "4b", result, mathematical_rigor_sequence, test_name)


test_help()
rigor()
vector()
trigonometrie()
mathematical_rigor()

gen_trace()

# def print_trace(trace):
#     for e in trace:
#         print("%s : %d, \"%s\"" % (e, trace[e][0], trace[e][1]))
# print_trace(trace)

os.system("rm -rf temp")
