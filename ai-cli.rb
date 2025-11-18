# typed: false
# frozen_string_literal: true

class AiCli < Formula
  desc "A cool AI CLI tool"
  
  # Include the Python Virtualenv helper methods (THIS IS THE FIX)
  include Language::Python::Virtualenv
  
  homepage "https://github.com/Codemaster-AR/homebrew-ai"
  url "https://github.com/Codemaster-AR/homebrew-ai/archive/refs/tags/v0.1.0.tar.gz"
  
  # 👇 CORRECTED SHA-256 (Found from your latest output) 👇
  sha256 "9c35f3ffbff580fa83d0d6aa720ef0b74e545f38f266739fbe087a336d9d1844"
  
  license "MIT"

  depends_on "python@3.12"

  def install
    # Now that the Python Virtualenv module is included, these methods will work.
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install_and_link buildpath 
  end

  test do
    # Ensure this version matches the actual output of your v0.1.0 release
    assert_match "AI CLI Version 1.5.0", shell_output("#{bin}/ai-cli version")
  end
end
