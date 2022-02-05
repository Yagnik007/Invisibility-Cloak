 l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv_frame, l_red, u_red)