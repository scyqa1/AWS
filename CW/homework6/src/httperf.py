from httperfpy import Httperf

for i in range(10,60,10):
    print 'Rate=' + str(i)
    perf = Httperf(server = "www.example.com", port = 8080, rate = i, num_calls = 50, num_conns = 100, timeout = 60, send_buffer = 4096, recv_buffer = 16384)

    perf.parser = True

    results = perf.run()

    print 'Request rate per sec, Connection rate per sec, Avg reply rate, Max reply rate, Response Time'
    print results["request_rate_per_sec"] + ', ' + results["connection_rate_per_se"] + ', ' + results["reply_rate_avg"] + ', ' + results["reply_rate_max"] + ', ' + results["reply_time_response"]
