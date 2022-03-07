CREATE TABLE apuestasProyecto.Users (

    user_id VARCHAR(64) NOT NULL DEFAULT UUID(),
    username VARCHAR(60) NOT NULL,
    mail VARCHAR(60) NOT NULL,
    cbu VARCHAR(60) NOT NULL,
    banco VARCHAR(60) NOT NULL,
    passwordd VARCHAR(80) NOT NULL,
    telefono VARCHAR(80) NOT NULL,
    intentos SMALLINT(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
	     

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (user_id),
    UNIQUE (username),
    UNIQUE (mail)
    
);


CREATE TABLE apuestasProyecto.misUsuarios (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id_corredor VARCHAR(64) NOT NULL,
    user_id_normal_user VARCHAR(64) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id_corredor) REFERENCES apuestasProyecto.Users(user_id),
    FOREIGN KEY (user_id_normal_user) REFERENCES apuestasProyecto.Users(user_id)

);

CREATE TABLE apuestasProyecto.beneficioAsignado (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id_corredor VARCHAR(64) NOT NULL,
    beneficio VARCHAR(10) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id_corredor) REFERENCES apuestasProyecto.Users(user_id)
);

CREATE TABLE apuestasProyecto.cuentaCorriente (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id VARCHAR(64) UNIQUE NOT NULL,
    saldo INT NOT NULL,
    creditoOtorgado INT NOT NULL,
    operaCredito VARCHAR(10) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id) REFERENCES apuestasProyecto.Users(user_id)
);
    


use apuestasProyecto;

INSERT INTO Users (username,mail,cbu,banco,passwordd,telefono,intentos,tipo) VALUES ('fransanti1','fransanti1@msn.com','0000000000000000000000','patagonia','sha256$kOqQhDmT$5af5ab1f85ebc65e285f9c74c861c28b67a599ec95eab9814c10c158efee09a8','342342',0,'super');

use apuestasProyecto;

INSERT INTO misUsuarios (user_id_corredor,username,mail,cbu,passwordd,intentos) VALUES ("f1c164d7-4d63-11eb-80bc-12704c653481",'santi','santi@msn.com','32423432','8923',0);

use apuestasProyecto;

INSERT INTO cuentaCorriente (user_id, saldo, creditoOtorgado, operaCredito) VALUES ("e2d0fe2f-60df-11eb-9e68-8cc84b63d8d9",30000,5000,"si");
INSERT INTO cuentaCorriente (user_id, saldo, creditoOtorgado, operaCredito) VALUES ("d46c0202-60df-11eb-9e68-8cc84b63d8d9",30000,5000,"si");


CREATE TABLE apuestasProyecto.Users (

    user_id VARCHAR(64) NOT NULL DEFAULT UUID(),
    username VARCHAR(60) NOT NULL,
    mail VARCHAR(60) NOT NULL,
    cbu VARCHAR(60) NOT NULL,
    banco VARCHAR(60) NOT NULL,
    passwordd VARCHAR(80) NOT NULL,
    telefono VARCHAR(80) NOT NULL,
    intentos SMALLINT(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
	     

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (user_id),
    UNIQUE (username),
    UNIQUE (mail)
    
);


CREATE TABLE apuestasProyecto.misUsuarios (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id_corredor VARCHAR(64) NOT NULL,
    user_id_normal_user VARCHAR(64) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id_corredor) REFERENCES apuestasProyecto.Users(user_id),
    FOREIGN KEY (user_id_normal_user) REFERENCES apuestasProyecto.Users(user_id)

);

CREATE TABLE apuestasProyecto.beneficioAsignado (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id_corredor VARCHAR(64) NOT NULL,
    beneficio VARCHAR(10) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id_corredor) REFERENCES apuestasProyecto.Users(user_id)
);

CREATE TABLE apuestasProyecto.cuentaCorriente (

    id_asociacion VARCHAR(64) NOT NULL DEFAULT UUID(),
    user_id VARCHAR(64) UNIQUE NOT NULL,
    saldo INT NOT NULL,
    creditoOtorgado INT NOT NULL,
    operaCredito VARCHAR(10) NOT NULL,
         

    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    PRIMARY KEY (id_asociacion),
    FOREIGN KEY (user_id) REFERENCES apuestasProyecto.Users(user_id)
);
    


use apuestasProyecto;

INSERT INTO Users (username,mail,cbu,banco,passwordd,telefono,intentos,tipo) VALUES ('fransanti1','fransanti1@msn.com','0000000000000000000000','patagonia','sha256$kOqQhDmT$5af5ab1f85ebc65e285f9c74c861c28b67a599ec95eab9814c10c158efee09a8','342342',0,'super');

use apuestasProyecto;

INSERT INTO misUsuarios (user_id_corredor,username,mail,cbu,passwordd,intentos) VALUES ("f1c164d7-4d63-11eb-80bc-12704c653481",'santi','santi@msn.com','32423432','8923',0);

use apuestasProyecto;

INSERT INTO cuentaCorriente (user_id, saldo, creditoOtorgado, operaCredito) VALUES ("e2d0fe2f-60df-11eb-9e68-8cc84b63d8d9",30000,5000,"si");
INSERT INTO cuentaCorriente (user_id, saldo, creditoOtorgado, operaCredito) VALUES ("d46c0202-60df-11eb-9e68-8cc84b63d8d9",30000,5000,"si");


