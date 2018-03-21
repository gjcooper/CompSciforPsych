# DRY# {{{
fixation.present()
exp.clock.wait(fixtime - first_stim.preload())
first_stim.present()
key, rt = exp.keyboard.wait(keys=trialkeys,
                            duration=trial_timeout)
fixation.present()
exp.clock.wait(fixtime - second_stim.preload())
second_stim.present()
key, rt = exp.keyboard.wait(keys=trialkeys,
                            duration=trial_timeout)
fixation.present()
exp.clock.wait(fixtime - third_stim.preload())
third_stim.present()
key, rt = exp.keyboard.wait(keys=trialkeys,
                            duration=trial_timeout)

# }}}

# Variable Names# {{{
list = ['sub01', 'sub02', 'sub03', 'sub04']
for l in list:
    print('Subject ID is ' + l)
    store.send(l, data[l])
# }}}

# Deep Nesting# {{{
def buildText(self):
    final_str = ''
    for section in cycle('1234'):
        if len(final_str) < self.textlength:
            final_str += section
        else:
            if self.reverseText:
                return reversed(final_str)
            else:
                return final_str

# }}}

# Too many Comments# {{{
# Grab the data
data = data_source.get_next_data_chunk()
# Clean the data
cleaned_data = remove_missing_rows(data)
# Run our analysis
analysed_data = analyse(cleaned_data)
# IF we want to display:
if display:
    # Show it onscreen
    plt.plot(analysed_data)
    plt.show()

# }}}

# Worst ever comment# {{{
def analyse_RTs(trials):
    '''Takes a list of trials (trial_type/RT) pairs and returns
    a dict where keys are trial_types and values are avgRT'''
    RTs_by_type = dict(); corr_by_type = dict()
    for trl, response, RT in trials:
        if trl in RTs_by_type:
            RTs_by_type[trl].append(RT)
            corr_by_type[trl].append(isCorrect(trial, response))
        else:
            RTs_by_type[trl] = [RT]
            corr_by_type[trl] = [isCorrect(trial, response)]
    RTavg = {k: mean(v) for k, v in RTs_by_type.iteritems()}
    percent_corr = {k: mean(v) for k, v in corr_by_type.iteritems()}
    return RTavg, percent_corr
# }}}

# Names of variables (Types, CamelCase, Hungarian etc)# {{{
class ClassName:
A_CONSTANT = 3.14

def function_name(variable_name):
    return A_CONSTANT * variable_name ** 2# }}}

# Whitespace# {{{
exp(trial[1], {response: 4})  # Good
exp( trial[ 1 ], { response: 4 } )  # Bad

if x == 4: print x, y; x, y = y, x  # Yes
if x == 4 : print x , y ; x , y = y , x  # No

x[3]  # Good
x [3]  # Bad# }}}

# Line Length# {{{
# Here is a long line
the_result = analysis_function(parameter1, parameter2, modifier=option1, display=True)
# }}}
