#!/bin/bash
# https://ubuntuforums.org/showthread.php?t=910717
B=$(tput bold)
N=$(tput sgr0)

one() {
  echo -e "${B}1. Create package structure...${N}"
  mkdir -p helloworld_1.0-1/usr/local/bin
  tree || true
  echo -e "\n"
}

two() {
  echo -e "${B}2. Creating exec...${N}"
  cat > helloworld_1.0-1/usr/local/bin/helloworld <<EOF
#!/bin/bash
echo HELLO
EOF
  chmod +x helloworld_1.0-1/usr/local/bin/helloworld
  cat helloworld_1.0-1/usr/local/bin/helloworld
  echo -e "\n"
}

three() {
  echo -e "${B}3. bash helloworld_1.0-1/usr/local/bin/helloworld...${N}"
  bash helloworld_1.0-1/usr/local/bin/helloworld
  echo -e "\n"
}

four() {
  echo -e "${B}4. Creating helloworld_1.0-1/DEBIAN/control metadata file${N}"
  mkdir -p helloworld_1.0-1/DEBIAN
  cat > helloworld_1.0-1/DEBIAN/control <<EOF
Package: helloworld
Version: 1.0-1
Section: base
Priority: optional
Architecture: i386
Depends: jq (>= 1.6)
Maintainer: Your Name <you@email.com>
Description: Hello World
 When you need some sunshine, just run this
 small program!
EOF
  cat helloworld_1.0-1/DEBIAN/control
  echo -e "\n"
}

five() {
  echo -e "${B}5. At last building package...${N}"
  dpkg-deb --build helloworld_1.0-1
  ls -l *.deb
  echo -e "\n"
}

six() {
  echo -e "${B}6. Install and test...${N}"
  sudo dpkg -i helloworld_1.0-1.deb
  echo -e "Test - exec helloworld from /usr/local/bin/helloworld"
  helloworld
  echo -e "\n"
}

echo -e "Hello in DEB build demo\n\n${N}"
one
two
three
four
five
six
