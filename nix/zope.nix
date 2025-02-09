{ sources ? import ../nix/sources.nix, mutwo-nix ? import (sources.mutwo-nix.outPath + "/nix/sources.nix") {}, pkgs ? import mutwo-nix.nixpkgs {}, pythonPackages ? pkgs.python310Packages}:
with pkgs;
with pythonPackages;



buildPythonPackage rec {
  name = "zope";
    src = fetchFromGitHub {
      owner = "zopefoundation";
      repo = "zope";
      # 5.11.1
      # rev = "db5cd4969cd86e061093873714d4423419f36efd";
      sha256 = "sha256-6lF4RAFENUwMklhkb3wuAKtGY+U5dDm6Tl+3fjYvJaw=";
    };
    checkPhase = ''
      runHook preCheck
      pytest
      runHook postCheck
    '';
    nativeCheckInputs = [
      # dev dependencies
      pytest
    ];
    propagatedBuildInputs = [
      # AccessControl
      # Acquisition
      btrees
      chameleon
      datetime
      # DocumentTemplate
      # ExtensionClass
      # MultiMapping
      pastedeploy
      persistent
      restrictedpython
      zconfig
      zodb
      setuptools
      transaction
      waitress
      # zExceptions
      # z3c.pt
      # zope.browser
      # zope.browsermenu
      # zope.browserpage
      # zope.browserresource
      # zope.component
      # zope.configuration
      # zope.container
      # zope.contentprovider
      # zope.contenttype
      # zope.datetime
      # zope.deferredimport
      # zope.event
      # zope.exceptions
      # zope.globalrequest
      # zope.i18n [zcml]
      # zope.i18nmessageid
      # zope-interface => but exists in newer nixpkgs
      # zope.lifecycleevent
      # zope.location
      # zope.pagetemplate
      # zope.processlifetime
      # zope.proxy
      # zope.ptresource
      # zope.publisher
      # zope.schema
      # zope.security
      # zope.sequencesort
      # zope.site
      # zope.size
      # zope.tal
      # zope.tales
      # zope.testbrowser
      # zope.testing
      # zope.traversing
      # zope.viewlet
      multipart
    ];
    doCheck = false;
}
