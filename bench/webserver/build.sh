#!/bin/bash

#builds nginx with specified openssl verison or build native and erimized

nginxloc=../../src/nginx
webbench=../../bench/webserver

#$1 openssl folder
build_nginx() {
    basename=`basename $1`
	
    basename=$basename$ccname	
    
    echo "building $basename"
    
    cd $nginxloc
    
    make clean
    
    ./configure "--prefix=$webbench/nginx-$basename/" --with-file-aio --without-http_rewrite_module --with-http_ssl_module "--with-openssl=$1" --with-ld-opt="$2" --with-cc-opt="-I ../erim/ -D_GNU_SOURCE" #--with-openssl-opt='-d' --with-debug
    
    make -j40 && make install
    
    cd -
}


# build common and erim library
make -s -C ../../src/common
make -s -C ../../src/erim


build_nginx ../openssl/native "../../bin/erim/liberim.a"
build_nginx ../openssl/erimized "../../bin/erim/liberim.a"
