def gallows():
  head = " 0 "
  arm_2_spaces = "/  "
  arm_torso_space = "/| "
  arm_torso_arm = "/|\ "
  fused_legs = " ^ "
  extended_legs = "/ \ "

  extremities = [head, arm_2_spaces, arm_torso_space, arm_torso_arm, fused_legs, extended_legs]
  
  while True:
    for _ in extremities:
      yield _
