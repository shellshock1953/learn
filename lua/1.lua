local foo = function(a, b)
    print("A: ", a)
    print("B: ", b)
end

foo(1, 2)

local func_with_opts = function(opts)
    local will_do_foo = opts.foo
    local filename = opts.filename
    print(will_do_foo, "--", filename)
end

func_with_opts { foo = true, filename = "hello.world" }
