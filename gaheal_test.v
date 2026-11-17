module gaheal_test(trace_in, led_out, buzzer);
  input trace_in;
  output led_out;
  output buzzer;
  assign led_out = trace_in;
  assign buzzer = ~trace_in;
endmodule
