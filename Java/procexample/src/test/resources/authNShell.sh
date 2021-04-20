#!/usr/bin/lua
local argparse = require "argparse"

local parser = argparse("authNShell.sh", "A mock for testing: second script.")
parser:option("-a --args", "Arguments.", "ARGS")
print "MOCK: authNShell-LUA"

local args = parser:parse()

local java_path = "/usr/lib/jvm/java-11-openjdk/bin/java"
local opts = "-jar resources/helloworld-1.0-SNAPSHOT.jar"
local main_class = "HelloWorld"
local cmd = string.format("%s %s %s", java_path, opts, main_class)

os.execute(cmd)
