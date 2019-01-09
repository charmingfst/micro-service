package org.chm.course.filter;

import org.chm.thrift.user.dto.UserDTO;
import org.chm.user.filter.LoginFilter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CourseFilter extends LoginFilter {
    @Override
    protected void login(HttpServletRequest request, HttpServletResponse response, UserDTO userDTO) {
        System.out.println("helloxxx");
        request.setAttribute("user", userDTO);
    }

}
