# NAME

Starwoman - because Starman does the same thing over and over again expecting different results

# VERSION

version 0.001

# SYNOPSIS

    # Run app.psgi with the default settings
    > starwoman

    # run with Server::Starter
    > start_server --port 127.0.0.1:80 -- starwoman --workers 32 myapp.psgi

    # UNIX domain sockets
    > starwoman --listen /tmp/starwoman.sock

Read more options and configurations by running \`perldoc starwoman\` (lower-case s).

# DESCRIPTION

Starwoman is a PSGI perl web server that has unique features such as:

- High Performance

    Uses the fast XS/C HTTP header parser

- Preforking

    Spawns workers preforked like most high performance UNIX servers
    do. Starwoman also reaps dead children and automatically restarts the
    worker pool.

- Signals

    Supports `HUP` for graceful worker restarts, and `TTIN`/`TTOU` to
    dynamically increase or decrease the number of worker processes, as
    well as `QUIT` to gracefully shutdown the worker processes.

- Superdaemon aware

    Supports [Server::Starter](https://metacpan.org/pod/Server::Starter) for hot deploy and graceful restarts.

- Multiple interfaces and UNIX Domain Socket support

    Able to listen on multiple interfaces including UNIX sockets.

- Small memory footprint

    Preloading the applications with `--preload-app` command line option
    enables copy-on-write friendly memory management. Also, the minimum
    memory usage Starwoman requires for the master process is 7MB and
    children (workers) is less than 3.0MB.

- PSGI compatible

    Can run any PSGI applications and frameworks

- HTTP/1.1 support

    Supports chunked requests and responses, keep-alive and pipeline requests.

- UNIX only

    This server does not support Win32.

# PERFORMANCE

Here's a simple benchmark using `Hello.psgi`.

    -- server: Starwoman (workers=10)
    Requests per second:    6849.16 [#/sec] (mean)
    -- server: Twiggy
    Requests per second:    3911.78 [#/sec] (mean)
    -- server: AnyEvent::HTTPD
    Requests per second:    2738.49 [#/sec] (mean)
    -- server: HTTP::Server::PSGI
    Requests per second:    2218.16 [#/sec] (mean)
    -- server: HTTP::Server::PSGI (workers=10)
    Requests per second:    2792.99 [#/sec] (mean)
    -- server: HTTP::Server::Simple
    Requests per second:    1435.50 [#/sec] (mean)
    -- server: Corona
    Requests per second:    2332.00 [#/sec] (mean)
    -- server: POE
    Requests per second:    503.59 [#/sec] (mean)

This benchmark was processed with `ab -c 10 -t 1 -k` on MacBook Pro
13" late 2009 model on Mac OS X 10.6.2 with perl 5.10.0. YMMV.

# NOTES

Because Starwoman runs as a preforking model, it is not recommended to
serve the requests directly from the internet, especially when slow
requesting clients are taken into consideration. It is suggested to
put Starwoman workers behind the frontend servers such as nginx, and use
HTTP proxy with TCP or UNIX sockets.

This is a fork of Starman for one particular reason: to stop the endless
forking of immediately dying children when app.psgi can't be loaded,
which flooded the log file and pegged the CPU. Starman hasn't been
maintained, hence the fork. Do not assume I will be any better about
maintaining this, considering how much attention I give to projects I
wrote myself.

# AUTHOR

Ashley Willis <awillis@synacor.com>

Tatsuhiko Miyagawa <miyagawa@bulknews.net> wrote [Starman](https://metacpan.org/pod/Starman), which this module
is a fork of with minimal modifications.

Andy Grundman wrote [Catalyst::Engine::HTTP::Prefork](https://metacpan.org/pod/Catalyst::Engine::HTTP::Prefork), which this module
is heavily based on.

Kazuho Oku wrote [Net::Server::SS::PreFork](https://metacpan.org/pod/Net::Server::SS::PreFork) that makes it easy to add
[Server::Starter](https://metacpan.org/pod/Server::Starter) support to this software.

# COPYRIGHT

Ashley Willis, 2019
Tatsuhiko Miyagawa, 2010-

# LICENSE

This library is free software; you can redistribute it and/or modify
it under the same terms as Perl itself.

# SEE ALSO

[Plack](https://metacpan.org/pod/Plack) [Catalyst::Engine::HTTP::Prefork](https://metacpan.org/pod/Catalyst::Engine::HTTP::Prefork) [Net::Server::PreFork](https://metacpan.org/pod/Net::Server::PreFork)
