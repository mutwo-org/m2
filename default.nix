let
  sourcesTarball = fetchTarball "https://github.com/mutwo-org/mutwo-nix/archive/refs/heads/main.tar.gz";
  m2 = import (sourcesTarball + "/m2/default.nix") {};
  m2-local = m2.overrideAttrs (
    finalAttrs: previousAttrs: {
       src = ./.;
    }
  );
in
  m2-local

