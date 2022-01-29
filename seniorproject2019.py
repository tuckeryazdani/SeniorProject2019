possible_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
possible_determinents = [1,3,5,7,9,11,15,17,19,21,23]
m11_solutions = []
m12_solutions = []
m21_solutions = []
m22_solutions = []
b1_solutions = []
b2_solutions = []
m11_solutions_second = []
m12_solutions_second = []
m21_solutions_second = []
m22_solutions_second = []
b1_solutions_second = []
b2_solutions_second = []

def compute_solutions_first_pair():
    for i in possible_values:
        m11 = possible_values[i]
        for j in possible_values:
            m12 = possible_values[j]
            for k in possible_values:
                b1 = possible_values[k]
                for l in possible_values:
                    m21 = possible_values[l]
                    for m in possible_values:
                        m22 = possible_values[m]
                        for n in possible_values:
                            b2 = possible_values[n]
                            solution_top = (m11+m12*18+b1)%26
                            solution_bottom = (m21+m21*18+b2)%26
                            if solution_top==24:
                                if solution_bottom==19:
                                    determinent = m11*m22-m12*m21
                                    if determinent in possible_determinents:
                                        m11_solutions.append(m11)
                                        m12_solutions.append(m12)
                                        m21_solutions.append(m21)
                                        m22_solutions.append(m22)
                                        b1_solutions.append(b1)
                                        b2_solutions.append(b2)

def compute_solutions_second_pair():
    for i in range(m11_solutions):
        m11=m11_solutions[i]
        for j in range(m12_solutions):
            m12=m12_solutions[j]
            for k in range(m21_solutions):
                m21=m21_solutions[k]
                for l in range(m22_solutions):
                    m22=m22_solutions[l]
                    for m in range(b1_solutions):
                        b1=b1_solutions[m]
                        for n in range(b2_solutions):
                            b2=b2_solutions[n]
                            solution_top = (m11+m12*18+b1)%26
                            solution_bottom = (m21+m21*18+b2)%26
                            if solution_top==0:
                                if solution_bottom==23:
                                    determinent=m11*m22-m12*m21
                                    if determinent in possible_determinents:
                                            m11_solutions_second.append(m11)
                                            m12_solutions_second.append(m12)
                                            m21_solutions_second.append(m21)
                                            m22_solutions_second.append(m22)
                                            b1_solutions_second.append(b1)
                                            b2_solutions_second.append(b2)
                                            
                            

compute_solutions_first_pair()
compute_solutions_second_pair()
print(m11_solutions)
print(m12_solutions)
print(b1_solutions)
