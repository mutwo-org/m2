{ sources ? import ./nix/sources.nix, rsources ? import (sources.mutwo-nix.outPath + "/nix/sources.nix"), pkgs ? import rsources.nixpkgs {}}:
with pkgs;
with pkgs.python311Packages;

let

  args = {sources=sources; pkgs=pkgs; pythonPackages=pythonPackages;};

  mutwo-abjad     = import (sources.mutwo-nix.outPath + "/mutwo.abjad/default.nix") {};
  mutwo-core = import (sources.mutwo-nix.outPath + "/mutwo.core/default.nix") {};
  mutwo-common = import (sources.mutwo-nix.outPath + "/mutwo.common/default.nix") {};
  mutwo-csound   = import (sources.mutwo-nix.outPath + "/mutwo.csound/default.nix") {};
  mutwo-ekmelily = import (sources.mutwo-nix.outPath + "/mutwo.ekmelily/default.nix") {};
  mutwo-midi     = import (sources.mutwo-nix.outPath + "/mutwo.midi/default.nix") {};
  mutwo-mmml     = import (sources.mutwo-nix.outPath + "/mutwo.mmml/default.nix") {};
  mutwo-music     = import (sources.mutwo-nix.outPath + "/mutwo.music/default.nix") {};
  mutwo-reaper = import (sources.mutwo-nix.outPath + "/mutwo.reaper/default.nix") {};
  mutwo-timeline = import (sources.mutwo-nix.outPath + "/mutwo.timeline/default.nix") {};

  #corigin = sources.mutwo-core;

in

  buildPythonPackage rec {
    name = "m2";
    src = ./.;
    nativeCheckInputs = [ pytest ];
    checkInputs = [ pytest ];
    propagatedBuildInputs = [ 
        mutwo-abjad
        mutwo-core
        mutwo-common
        mutwo-csound
        mutwo-ekmelily
        mutwo-midi
        mutwo-mmml
        mutwo-music
        mutwo-reaper
        mutwo-timeline
    ];
    checkPhase = ''
      runHook preCheck
      pytest
      runHook postCheck
    '';
    doCheck = true;
    format = "pyproject";
  }
