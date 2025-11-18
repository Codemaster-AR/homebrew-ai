# typed: false
# frozen_string_literal: true

class AiCli < Formula
  desc "A cool AI CLI tool"
  homepage "https://github.com/Anay_Rustogi/AI_CLI"
  url "https://github.com/Anay_Rustogi/AI_CLI/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "PASTE_THE_SHA256_OF_THE_TAR_GZ_FILE_HERE" # IMPORTANT
  license "MIT" # Or whatever license you use

  depends_on "python@3.12"

  def install
    # This is a common pattern for Python tools.
    # It creates a virtual environment and installs the tool and its dependencies into it.
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install_and_link buildpath

    # The line above is a shortcut for the following:
    # system libexec/"bin/pip", "install", "."
    # bin.install_symlink libexec/"bin/ai-cli" => "ai-cli"
  end

  test do
    # This test will run `ai-cli --version` and check the output.
    assert_match "AI CLI Version 1.5.0", shell_output("#{bin}/ai-cli version")
  end
end
