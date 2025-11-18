# typed: false
# frozen_string_literal: true

class AiCli < Formula
  desc "A cool AI CLI tool"
  
  # Includes Python helper methods for virtual environments (fixed NoMethodError)
  include Language::Python::Virtualenv
  
  # IMPORTANT: The version is now incremented to reflect the new source code with dependencies
  version "0.1.1" 
  
  homepage "https://github.com/Codemaster-AR/homebrew-ai"
  
  # The URL now points to the new tag (v0.1.1)
  url "https://github.com/Codemaster-AR/homebrew-ai/archive/refs/tags/v0.1.1.tar.gz" 
  
  # 👇 FINAL CORRECTED SHA256 👇
  sha256 "7ff28f66a64d871f456ce3a926dd5d6753c7f48feb6f0bf5eff8e1dda2fdc4d8" 
  
  license "MIT"

  depends_on "python@3.12"

  def install
    # This creates a virtual environment and installs the package and its dependencies (including groq)
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install_and_link buildpath 
  end

  test do
    # You may need to change "1.5.0" to match the actual version output of your tool
    assert_match "AI CLI Version 1.5.0", shell_output("#{bin}/ai-cli version")
  end
end
