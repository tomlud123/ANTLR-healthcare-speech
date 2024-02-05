grammar test;

input : {priorities.get("rule_a_z", 0) >= priorities.get("rule_a_x", 0) && priorities.get("rule_a_z", 0) >= priorities.get("rule_a_g", 0)}? [a-z]
      | {priorities.get("rule_a_x", 0) > priorities.get("rule_a_z", 0) && priorities.get("rule_a_x", 0) >= priorities.get("rule_a_g", 0)}? [a-x]
      | [a-g] ;

rule_a_x: W1;
rule_a_z: W2;
rule_a_g: W3;

W1: [a-x]+;
W2: [a-z]+;
W3: [a-g]+;