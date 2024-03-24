import { useCallback } from "react";
import "./IPhone14Plus.css";

const IPhone14Plus = () => {
  const onButtonContainerClick = useCallback(() => {
    // Please sync "iPhone 14 Plus - 3" to the project
  }, []);

  return (
    <div className="iphone-14-plus-2">
      <div className="content-parent">
        <div className="content">
          <div className="copy">
            <div className="create-an-account">Create an account</div>
            <div className="enter-your-email">
              Enter your email to sign up for this app
            </div>
          </div>
          <div className="input-and-button">
            <div className="field">
              <div className="label">email@domain.com</div>
            </div>
            <div className="button" onClick={onButtonContainerClick}>
              <div className="primary">Sign up with email</div>
            </div>
          </div>
          <div className="divider">
            <div className="divider1" />
            <div className="or-continue-with">or continue with</div>
            <div className="divider1" />
          </div>
          <div className="button1">
            <div className="label1">
              <img className="google-icon" alt="" src="/google.svg" />
              <div className="primary">Google</div>
            </div>
          </div>
          <div className="by-clicking-continue-container">
            <span>{`By clicking continue, you agree to our `}</span>
            <span className="terms-of-service">Terms of Service</span>
            <span>{` and `}</span>
            <span className="terms-of-service">Privacy Policy</span>
          </div>
        </div>
        <img className="image-3-icon" alt="" src="/image-3@2x.png" />
        <div className="status-bar-iphone-x-or-newe">
          <img className="notch-icon" alt="" src="/notch@2x.png" />
          <div className="right-side">
            <img className="battery-icon" alt="" src="/battery.svg" />
            <img className="wifi-icon" alt="" src="/wifi.svg" />
            <img
              className="mobile-signal-icon"
              alt=""
              src="/mobile-signal.svg"
            />
            <img
              className="recording-indicator-icon"
              alt=""
              src="/recording-indicator.svg"
            />
          </div>
          <img className="left-side-icon" alt="" src="/left-side.svg" />
        </div>
        <img className="image-3-icon" alt="" src="/image-3@2x.png" />
        <div className="status-bar-iphone-x-or-newe">
          <img className="notch-icon" alt="" src="/notch@2x.png" />
          <div className="right-side">
            <img className="battery-icon" alt="" src="/battery.svg" />
            <img className="wifi-icon" alt="" src="/wifi.svg" />
            <img
              className="mobile-signal-icon"
              alt=""
              src="/mobile-signal.svg"
            />
            <img
              className="recording-indicator-icon"
              alt=""
              src="/recording-indicator.svg"
            />
          </div>
          <img className="left-side-icon" alt="" src="/left-side.svg" />
        </div>
      </div>
    </div>
  );
};

export default IPhone14Plus;
