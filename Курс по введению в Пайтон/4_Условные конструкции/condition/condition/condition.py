is_ready = True

if is_ready:
    state_msg = 'Ready'
else:
    state_msg = 'Not ready'

print(state_msg)

print(is_ready and 'Ready' or 'Not ready')

print('Ready' if is_ready else 'Not ready')

