# Script that installs a package, here: puppet-flask
package { 'puppet-lint flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
