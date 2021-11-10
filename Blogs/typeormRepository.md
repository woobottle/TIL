# TypeOrm Repository API

목차     
[typeOrm 연결](#typeorm-연결)    
[모델 선언](#모델-선언)    
[관계 선언](#관계-선언)    
[repositoryApi 사용](#repositoryapi-사용)    
[디버그 사항](#디버그-사항)    

------

* typeOrm은 자바스크립트 진영에서 사용하는 ORM 입니다.    
* Rails에는 ActiveRecord, 자바 진영에는 JPA 등등이 있을거에요, typeOrm의 유사품으로 Sequelize도 있어요     
* Sequelize는 ActiveRecord와 쓰임이 유사하다고 해요     

**저는 typeOrm과 Sequelize중 typeOrm을 선택했습니다.**   

1. typeOrm이 typescript와 호환이 좀 더 잘된다고 접하였습니다     
2. Sequelize에 비해 간소화되어 있다고 생각했습니다     
3. npm download수는 typeOrm이 적지만 슬랙, 깃헙등 소통이 더 활성화 되어있다고 느꼈습니다.     

간단한 typeorm 사용법과 최근 발생한 이슈사항에 대해 정리 하겠습니다.     

### typeOrm 연결
---

nest에서는 아래와 같이 사용했습니다

```js
import { ConnectionOptions } from 'typeorm';
import {
  DB_HOST,
  DB_PORT,
  DB_USERNAME,
  DB_DATABASE,
  DB_PASSWORD,
} from '@environments';

export const typeormOptions: ConnectionOptions = {
  type: 'postgres',
  host: DB_HOST,
  port: DB_PORT,
  username: DB_USERNAME,
  database: DB_DATABASE,
  password: DB_PASSWORD,
  entities: [`${__dirname}/../../**/*.entity.{js,ts}`],
  synchronize: true,
};

```

```js
Module({
  imports: [
    ServeStaticModule.forRoot({
      rootPath: join(__dirname, '..', STATIC),
    }),
    AdminModule.createAdmin(adminOptions),
    TypeOrmModule.forRoot(typeormOptions),
    //....
});
export class AppModule {}
```

```js
const app = await NestFactory.create<NestExpressApplication>(AppModule);
await app.listen(port);
```

express에서는 아래와 같이 사용하면 될거에요

```js
import "reflect-metadata";
import { createConnection } from "typeorm";
import { User } from "./entity/Photo";

createConnection({
    type: "postgresql",
    host: "localhost",
    port: 5432,
    username: "root",
    password: "",
    database: "test",
    entities: [
      User
    ],
    synchronize: true,
    logging: false
}).then(connection => {
    // here you can start to work with your entities
}).catch(error => console.log(error));

app.listen(port);
```


### 모델 선언
----

클래스를 정의하고 @Entity() 데코레이터를 사용해주시면 접근할 수 있습니다.      
기본적인 정의도 같이 포함된 예시로 첨부하겠습니다.(ex. PrimaryGeneratedColumn, Column)     
세부 옵션들이 많은데 문서를 참고하시는게 더 좋으실 거에요         
아래 클래스 이름의 예시는 제가 사용했던 방식이라 자유롭게 변경하셔도 됩니다      

```js
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';
import { UserType } from './enum';

// Naming을 추가해줄수도 있습니다, 추가된 이름으로 디비에 생성되고 접근 됩니다.
@Entity('users') 
export class UsersEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  email: string;

  @Column()
  name: string;

  @Column()
  age: number;

  @Column({
    type: 'enum',
    enum: UserType,
    default: UserType.NORMAL,
  })
  user_type: UserType;
}
```


### 관계-선언
----
many-to-one, one-to-many, one-to-one, many-to-many 과 같은 정의를 할수 있습니다.    

rails의 has_many, has_one과 같은 개념이라고 생각하시면 됩니다.    

many-to-many의 경우 중간테이블을 자동으로 생성해 주는데 제가 프로젝트에서 사용할때는 배제하였습니다.   
1. 클래스 없이 사용하는 것이 해당 모델의 존재유무를 파악하기 힘들었습니다. @Many-to-Many 데코레이터의 유무로만 존재하니 존재유무를 파악하기 쉽지 않더라구요    
2. 커스터마이징 하기가 어렵거나 불가능했습니다. 저같은 경우 중간테이블에 칼럼을 추가해서 사용하는 편이 많은데 이러한 경우 불편한 점이 많았습니다.    

아래는 사용 예시입니다.

```js
@Entity('users')
export class UsersEntity {
  //...

  @OneToMany((_) => UsersChatroomsEntity, (usersChatrooms) => usersChatrooms.user)
  userChatrooms: UserChatroomsEntity[];  

  @OneToOne((type) => BusesEntity, (bus) => bus.user)
  @JoinColumn({ name: 'bus_id' })
  bus: BusesEntity;
}

@Entity('users_chatrooms')
export class UsersChatroomsEntity extends DateAuditEntity {
  @ManyToOne((_) => UsersEntity, (user) => user.userChatrooms)
  @JoinColumn({ name: 'user_id', referencedColumnName: 'id' })
  user: UsersEntity;
}


@Entity('buses')
export class BusesEntity {
  //..

  @OneToOne((type) => UsersEntity, (user) => user.bus)
  @JoinColumn({ name: 'user_id' })
  user: UsersEntity;
}
```

JoinColumn을 설정해주면 추가된 테이블에 외래키를 자동으로 설정해 줍니다.      
property의 name은 이름을 커스터마이징 하기 위한 것입니다.     

OneToOne의 관계에선 JoinColumn()을 필수로 지정해주어야 합니다.     

ManyToOne과 OneToMany의 관계에선 필수가 아닙니다.     



### repositoryApi 사용
-----

orm의 실사용 예시 입니다.     

typeorm에서 제공해주는 api도 있고(이를 repositoryApi로 지칭 하겠습니다)      
직접 쿼리를 만들수 있는 queryBuilder 또한 제공해 줍니다.     
저는 최대한 repository api의 사용을 지향하고 이 api로 처리가 안될때 쿼리빌더를 이용하여 사용하곤 했습니다   
기본적인 사용예시만 첨부하겠습니다. 디테일한 내용들은 문서를 보시는게 훨씬 좋습니다.   

nest에서의 사용 예시

```js
export class UsersService {
  constructor(
    @InjectRepository(Users)
    private readonly usersRepository: Repository<Users>,

    @InjectRepository(Months)
    private readonly monthsRepository: Repository<Months>,

    @InjectRepository(Buses)
    private readonly busesRepository: Repository<Buses>,
  )

  async getObject(id: number): Promise<UsersEntity> {
    const user = this.usersRepository.findOne({
      where: {
        id,
      },
    });
    
    return user;
  };

  async test() {
    await this.busesRepository.update(
       { user },
       {
         ...profileImg,
         user,
         imagable_type: 'user',
         imagable_id: user.id,
       },
     );

    await this.busesRepository.save({
       user,
     });

    const busProfileImages = await this.busesRepository.find({
        key: In([...busProfileKeys]),
      });
    return busProfileImages;
  }
}
```

아래는 쿼리빌더의 사용 예시 입니다.

```js
const drivers = await getRepository(UsersEntity)
      .createQueryBuilder('users')
      .where(`drivable_region @> ARRAY['${region}']`)
      .andWhere(
        new Brackets((qb) => {
          qb.where('user_type = :driver', { driver: 'driver' });
        }),
      )
      .andWhere('users.name ilike :name', { name: `%${searchBy}%` })
      .leftJoinAndSelect('users.bus', 'buses')
      .leftJoinAndSelect('users.profile', 'profile')
      .orderBy(orderQuery)
      .take(5)
      .skip(5 * (page - 1))
      .getMany();

    return drivers;
```

직접 커스터마이징 할수 있는 내용들이 많아서 더 고도화된 작업을 진행할 수 있습니다.     


## 디버그 사항
----

typeorm의 repositoryApi를 사용하는 경우 find의 relation 파라미터를 이용하는 경우가 있습니다.    
이때 one-to-many, many-to-one 어디에서 접근하냐에 따라 에러가 발생할 수 있습니다.   
이곳에서 시간을 많이 사용해서 다른 분들은 저와 같은 상황에 마주치지 않길 바랍니다    

```js
const user_chatrooms = await getRepository(UsersChatroomsEntity).find({
  relations: ['chatroom', 'user'],
  where: {
    user: {
      id: currentUser?.id || 301,
    },
  },
});
```

relation에 포함된 테이블의 칼럼으로 쿼리문을 생성할 수 있습니다.    

하지만 아래는 에러상황 입니다    

```js
const chatrooms = await this.find({
  relations: ['usersChatrooms'],
  where: {
    userChatrooms: {
      id: 61,
    },
  },
});
return chatrooms;
```

위 에러코드는 chatroom에 userChatrooms 칼럼이 없다고 에러를 발생시킵니다    
where문을 없애면 결과는 나오지만 모든 채팅방에 userChatroom이 조인된채 결과가 나옵니다.     
이건 우리가 원하는 결과가 아닙니다     

제가 추측하기론 외래키의 유무가 위의 에러를 발생시키는 것 같습니다.   

아래는 chatroom과 userChatroom의 관계 설정 입니다.    

```js
@Entity('users_chatrooms')
export class UsersChatroomsEntity {
  //..

  @ManyToOne((_) => ChatroomsEntity, (chatroom) => chatroom.userChatrooms)
  @JoinColumn({ name: 'chatroom_id', referencedColumnName: 'id' })
  chatroom: ChatroomsEntity;

  @ManyToOne((type) => UsersEntity, (user) => user.userChatrooms)
  @JoinColumn({ name: 'user_id', referencedColumnName: 'id' })
  user: UsersEntity;
}

@Entity('chatrooms')
export class ChatroomsEntity {
  //... 

  @OneToMany(
    (type) => UsersChatroomsEntity,
    (userChatrooms) => userChatrooms.chatroom,
  )
  userChatrooms: UsersChatroomsEntity[];
}
```
     
**many-to-one에서는 joinColumn을 이용, repositoryApi내의 where문 안에서 접근이 가능하나      
one-to-many에서 relations으로 접근시에는 해당 테이블의 칼럼에 접근이 안되는 것 같습니다.**    

결국 이 상황은 쿼리 빌더를 사용해서 해결하였습니다.    

```js
const chatroom = await getRepository(ChatroomsEntity)
      .createQueryBuilder('chatroom')
      .leftJoin('chatroom.userChatrooms', 'userChatrooms')
      .leftJoin('userChatrooms.user', 'user')
      .where('chatroom.id IN (:...chatroom_ids)')
      .andWhere('user.uuid = :uuid', { uuid: userUuid })
      .setParameters({ chatroom_ids })
      .getOne();
```

아래 링크는 쿼리빌더의 사용예시 + 테스트 코드 나와있는 깃헙 입니다.      
<https://github.com/typeorm/typeorm/blob/master/test/functional/query-builder/join/query-builder-joins.ts>

출처: <https://typeorm.io/#/>