addpath('IntLinInc2D');
addpath('IntLinInc3D');


disp('_____________________________First_Part_____________________________')

Aconst2 = [4 1;
    3 7;
    5 6]';
A2 = [infsup(3,5) infsup(-1,3);
    infsup(1,5) infsup(6,8);
    infsup(2,8) infsup(4,8)]';
x2 = [1;
    1;
    -1];
bconst2 = Aconst2 * x2;
b2 = [infsup(1,3);
    infsup(0,4)];

Cminim2 = cond(inf(A2));
MatrixM2 = [0 0;
    0 0;
    0 0];
b12 = inf(A2);

for i1=inf(A2(1,1)):(sup(A2(1,1))-inf(A2(1,1))):sup(A2(1,1))
    for i2=inf(A2(1,2)):(sup(A2(1,2))-inf(A2(1,2))):sup(A2(1,2))
        for i3=inf(A2(1,3)):(sup(A2(1,3))-inf(A2(1,3))):sup(A2(1,3))
            for j1=inf(A2(2,1)):(sup(A2(2,1))-inf(A2(2,1))):sup(A2(2,1))
                for j2=inf(A2(2,2)):(sup(A2(2,2))-inf(A2(2,2))):sup(A2(2,2))
                    for j3=inf(A2(2,3)):(sup(A2(2,3))- inf(A2(2,3))):sup(A2(2,3))
                        if cond([i1 i2 i3;j1 j2 j3])<=b12
                            Cminim2=cond([i1 i2 i3;j1 j2 j3]);
                            MatrixM2=[i1 i2 i3;j1 j2 j3];
                        end
                    end
                end
            end
        end
    end
end

disp('Cmin1=')
disp(Cminim2)
disp('Matrix1=')
disp(MatrixM2)
disp('__________________')

%[maxTol2,argmaxTol2,envs2,ccode2] = tolsolvty(inf(A2),sup(A2),inf(b2),sup(b2))
maxTol2 = 0.34374927;
argmaxTol2 = [4.06249616e-01;
 1.25000148e-01;
 1.37765665e-07];
ive2 = sqrt(2) * Cminim2 * maxTol2 * (norm(argmaxTol2) / norm(mid(b2)))
Xsolv2 = [argmaxTol2 - ive2, argmaxTol2 + ive2]

[Z] = EqnTol3D(inf(A2),sup(A2),inf(b2),sup(b2),1,1)
hold on
scatter3(argmaxTol2(1), argmaxTol2(2), argmaxTol2(3), 'm*');
scatter3(x2(1), x2(2), x2(3), 'b+');

plot3([Xsolv2(1,1) Xsolv2(1,2)], [Xsolv2(2,1)  Xsolv2(2,1)], [Xsolv2(3,1) Xsolv2(3,1)], 'black');
plot3([Xsolv2(1,1) Xsolv2(1,2)], [Xsolv2(2,2)  Xsolv2(2,2)], [Xsolv2(3,1) Xsolv2(3,1)], 'black');
plot3([Xsolv2(1,1) Xsolv2(1,2)], [Xsolv2(2,1)  Xsolv2(2,1)], [Xsolv2(3,2) Xsolv2(3,2)], 'black');
plot3([Xsolv2(1,1) Xsolv2(1,2)], [Xsolv2(2,2)  Xsolv2(2,2)], [Xsolv2(3,2) Xsolv2(3,2)], 'black');

plot3([Xsolv2(1,1) Xsolv2(1,1)], [Xsolv2(2,1)   Xsolv2(2,2)], [Xsolv2(3,1) Xsolv2(3,1)], 'black');
plot3([Xsolv2(1,1) Xsolv2(1,1)], [Xsolv2(2,1)   Xsolv2(2,2)], [Xsolv2(3,2) Xsolv2(3,2)], 'black');
plot3([Xsolv2(1,2) Xsolv2(1,2)], [Xsolv2(2,1)   Xsolv2(2,2)], [Xsolv2(3,1) Xsolv2(3,1)], 'black');
plot3([Xsolv2(1,2) Xsolv2(1,2)], [Xsolv2(2,1)   Xsolv2(2,2)], [Xsolv2(3,2) Xsolv2(3,2)], 'black');

plot3([Xsolv2(1,1) Xsolv2(1,1)], [Xsolv2(2,1)  Xsolv2(2,1)], [Xsolv2(3,1) Xsolv2(3,2)], 'black');
plot3([Xsolv2(1,1) Xsolv2(1,1)], [Xsolv2(2,2)  Xsolv2(2,2)], [Xsolv2(3,1) Xsolv2(3,2)], 'black');
plot3([Xsolv2(1,2) Xsolv2(1,2)], [Xsolv2(2,1)  Xsolv2(2,1)], [Xsolv2(3,1) Xsolv2(3,2)], 'black');
plot3([Xsolv2(1,2) Xsolv2(1,2)], [Xsolv2(2,2)  Xsolv2(2,2)], [Xsolv2(3,1) Xsolv2(3,2)], 'black');

Title_str = 'Недоопределённая ИСЛАУ: допусковое множество решений';
title(Title_str);
[m, n] = size(Aconst2);
xlabel('\it x_1');
ylabel('\it x_2');
zlabel('\it x_3');
title_str_name = strcat('islau solution', ' ', num2str(m), 'x', num2str(n))
figure_name_out = strcat(title_str_name,'.png')
print('-dpng', '-r300', figure_name_out), pwd




disp('_____________________________Second_Part_____________________________')

Aconst = [4 1;
    3 7;
    5 6];
A = [infsup(3,5) infsup(-1,3);
    infsup(1,5) infsup(6,8);
    infsup(2,8) infsup(4,8)];
x = [1;
    -1];
bconst = Aconst * x;
b = [infsup(0,6);
    infsup(-9,1);
    infsup(-7,5)];

[V, P1, P2, P3, P4] = EqnTol2D(inf(A),sup(A),inf(b),sup(b));

Cminim=cond(inf(A));
b1=inf(A);
for i1=inf(A(1,1)):(sup(A(1,1))-inf(A(1,1))):sup(A(1,1))
    for i2=inf(A(1,2)):(sup(A(1,2))-inf(A(1,2))):sup(A(1,2))
        for j1=inf(A(2,1)):(sup(A(2,1))-inf(A(2,1))):sup(A(2,1))
            for j2=inf(A(2,2)):(sup(A(2,2))-inf(A(2,2))):sup(A(2,2))
                for k1=inf(A(3,1)):(sup(A(3,1))-inf(A(3,1))):sup(A(3,1))
                    for k2=inf(A(3,2)):(sup(A(3,2))-inf(A(3,2))):sup(A(3,2))
                        if cond([i1 i2;j1 j2;k1 k2])<=b1
                            Cminim=cond([i1 i2;j1 j2;k1 k2]);
                        end
                    end
                end
            end
        end
    end
end

disp('Cmin2=')
disp(Cminim)
disp('__________________')

maxTol = 0.62790687;
argmaxTol = [0.88372067;
    -0.67441837];
ive = sqrt(2) * Cminim * maxTol * (norm(argmaxTol) / norm(mid(b)))
Xsolv = [argmaxTol - ive, argmaxTol + ive]

rectangle('Position',[Xsolv(1,1) Xsolv(2,1) Xsolv(1,2)-Xsolv(1,1) Xsolv(2,2)-Xsolv(2,1) ])
rectangle('Position',[argmaxTol(1) argmaxTol(2) 0.003 0.003 ],'EdgeColor','r')
text(argmaxTol(1)+0.02,argmaxTol(2),'argmaxTol','FontSize',8)
Title_str = 'Переопределённая ИСЛАУ: допусковое множество решений';
title(Title_str);
[m, n] = size(Aconst);
xlabel('\it x_1');
ylabel('\it x_2');
title_str_name = strcat('islau solution', ' ', num2str(m), 'x', num2str(n));
figure_name_out = strcat(title_str_name,'.png');
print('-dpng', '-r300', figure_name_out), pwd