./createContent.sh
sudo mount -o remount,size=5G /dev/shm
mkdir -p /dev/shm/html
cp content/* /dev/shm/html

echo "Unprotected"
sudo taskset -c 1 ./nginx-native/sbin/nginx -c ../conf/nginx.conf.1 &
sleep 1
ab -k -t 5 -c 100 -n 200000000   https://localhost/128kb >> /dev/null # Warmup run 
echo "----0kb" > native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/0kb >> native.log
echo "----1kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/1kb >> native.log
echo "----2kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/2kb >> native.log
echo "----4kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/4kb >> native.log
echo "----8kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/8kb >> native.log
echo "----16kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/16kb >> native.log
echo "----32kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/32kb >> native.log
echo "----64kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/64kb >> native.log
echo "----128kb" >> native.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/128kb >> native.log
sudo pkill nginx
echo "ERIM"
sudo taskset -c 1 ./nginx-erimized/sbin/nginx -c ../conf/nginx.conf.1 &
sleep 1
ab -k -t 5 -c 100 -n 200000000   https://localhost/128kb >> /dev/null # Warmup run
echo "----0kb" > erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/0kb >> erim.log
echo "----1kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/1kb >> erim.log
echo "----2kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/2kb >> erim.log
echo "----4kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/4kb >> erim.log
echo "----8kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/8kb >> erim.log
echo "----16kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/16kb >> erim.log
echo "----32kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/32kb >> erim.log
echo "----64kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/64kb >> erim.log
echo "----128kb" >> erim.log
ab -k -t $1 -c 100 -n 200000000   https://localhost/128kb >> erim.log
sudo pkill nginx
