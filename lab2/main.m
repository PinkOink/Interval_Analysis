    function main
    
    % Минимизация функции Растригина
    X = [ infsup(-5,5) ; infsup(-5,5) ];
    [Z, WL, widths, extrems, centers] = globopt0(X, @ObjRastriginFunc);
    
    N = 1:1:length(widths);
    
    figure()
    plot(N, widths);
    title('Зависимость ширины ведущего блока от числа итераций (функция Растригина)')
    xlabel('Итерация')
    ylabel('Ширина ведущего блока')
    
    figure()
    semilogy(N, widths);
    title('Зависимость ширины ведущего блока от числа итераций (функция Растригина)')
    xlabel('Итерация')
    ylabel('Ширина ведущего блока')
    
    disp("Rastrigin Func")
    disp("min f(x, y) = " + Z)


    % Минимизация функции МакКормика
    X = [ infsup(-1.5,4) ; infsup(-3,4) ];
    [Z, WL, widths, extrems, centers] = globopt0(X, @ObjMcCormickFunc);
    
    N = 1:1:length(widths);
    
    figure()
    plot(N, widths);
    title('Зависимость ширины ведущего блока от числа итераций (функция МакКормика)')
    xlabel('Итерация')
    ylabel('Ширина ведущего блока')
    
    figure()
    semilogy(N, widths);
    title('Зависимость ширины ведущего блока от числа итераций (функция МакКормика)')
    xlabel('Итерация')
    ylabel('Ширина ведущего блока')
    
    disp("McCormick Func")
    disp("min f(x, y) = " + Z)
    
    figure()
    solution = -1.9133;
    N = 1:1:length(extrems);
    errors = abs(extrems - solution);
    plot(N(1:end), errors(1:end));
    title('Зависимость полученного значения экстремума от числа итераций')
    xlabel('Итерация')
    ylabel('Погрешность полученного решения')

    figure()
    semilogy(N(1:end), errors(1:end));
    title('Зависимость полученного значения экстремума от числа итераций')
    xlabel('Итерация')
    ylabel('Погрешность полученного решения')
    
    figure()
    x = linspace(-1.5,0.5);
    y = linspace(-3,-0.5);
    [X,Y] = meshgrid(x,y);
    Z = sin(X + Y) + sqr(X - Y) - 1.5 * X + 2.5 * Y + 1;
    contour(X,Y,Z,70)
    hold on
    plot(centers((end - 50):end,1), centers((end - 50):end,2),'-*')
    title('Траектория центров последних 50 брусков')
    xlabel('X')
    ylabel('Y')
    
    figure()
    contour(X,Y,Z,70)
    hold on
    plot(centers((end - 100):end,1), centers((end - 100):end,2),'*')
    title('Центры последних 100 брусков')
    xlabel('X')
    ylabel('Y')
    
    end
    
    function Y = ObjRastriginFunc(X)
    %   естественное интервальное расширение целевой функции Растригина
        Y = sqr(X(1)) + sqr(X(2)) - cos(18*X(1)) - cos(18*X(2));
    end
    
    function Y = ObjMcCormickFunc(X)
    %   естественное интервальное расширение целевой функции МакКормика
        Y = sin(X(1) + X(2)) + sqr(X(1) - X(2)) - 1.5 * X(1) + 2.5 * X(2) + 1;   
    end
